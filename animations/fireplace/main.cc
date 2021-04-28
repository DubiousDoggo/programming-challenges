#include <SDL2/SDL.h>
#include <chrono>
#include <cstring>
#include <iostream>
#include <random>
#include <string>
using namespace std::string_literals;

const int DEFAULT_WINDOW_WIDTH = 1200;
const int DEFAULT_WINDOW_HEIGHT = 800;

int modulo(int a, int b) {
    int m = a % b;
    if (m < 0)
        m = (b < 0) ? m - b : m + b;
    return m;
}

void cleanup(SDL_Window *&window, SDL_Renderer *&renderer) {
    SDL_DestroyRenderer(renderer);
    renderer = nullptr;
    SDL_DestroyWindow(window);
    window = nullptr;
    SDL_Quit();
}

std::mt19937 random(std::chrono::system_clock::to_time_t(std::chrono::system_clock::now()));
std::uniform_real_distribution real;

const int nflames = 512;
static struct { int x, y, i; } flames[nflames];

float wind_direction = 0.35;
float particle_wiggle = 0.40;

float flame_chance = 0.50;
float flame_float = 0.90;
float flame_intensity_drop = 0.52;
float flame_dropoff = 0.90;

float ember_threshold = 0.61;
float ember_float = 0.20;
float ember_glow = 0.50;
float ember_flicker_chance = 0.40;
int ember_flicker_amount = 2;

const int nflame_colors = 8;
// idle color then increasing intensity
const uint32_t flame_color_table[nflame_colors] = {0xFFFFFFEE, 0xFFA10100, 0xFFDA1F05, 0xFFFF882D, 0xFFFFAA4D, 0xFFFFD37A, 0xFFF9F687, 0xFFFFFFEE}; // soft
// const uint32_t flame_color_table[nflame_colors] = {0xFFFFFFEE, 0xFFA10100, 0xFFDA1F05, 0xFFF33C04, 0xFFFE650D, 0xFFFFC11F, 0xFFFFF75D, 0xFFFFFFEE}; // retro

void init_fire(SDL_Surface *surface) {
    for (int i = 0; i < nflames; i++)
        flames[i] = {std::uniform_int_distribution(0, surface->w - 1)(random), surface->h - 1, 0};
}

void fire_effect(SDL_Surface *surface) {

    auto *pixels = (uint32_t *)surface->pixels;

    // fade out top area
    for (int y = 0; y < surface->h * ember_threshold; y++) {
        float fade = ember_glow;
        for (int x = 0; x < surface->w; x++) {
            uint8_t r, g, b;
            SDL_GetRGB(pixels[x + surface->w * y], surface->format, &r, &g, &b);
            pixels[x + surface->w * y] = SDL_MapRGB(surface->format, r * fade, g * fade, b * fade);
        }
    }

    // fade out existing pixels in the flames
    for (int y = surface->h * ember_threshold; y < surface->h; y++) {
        float fade = flame_dropoff + (1 - flame_dropoff) * y / surface->h;
        for (int x = 0; x < surface->w; x++) {
            uint8_t r, g, b;
            SDL_GetRGB(pixels[x + surface->w * y], surface->format, &r, &g, &b);
            pixels[x + surface->w * y] = SDL_MapRGB(surface->format, r * fade, g * fade, b * fade);
        }
    }

    // update particles
    for (int i = 0; i < nflames; i++) {
        if (flames[i].i != 0) {
            if (flames[i].y < surface->h * ember_threshold) {
                // embers
                if (flames[i].i < nflame_colors - ember_flicker_amount)
                    flames[i].i++;

                if (real(random) < ember_flicker_chance)
                    flames[i].i -= ember_flicker_amount;

                if (real(random) < ember_float)
                    flames[i].y--;

            } else {
                // flames
                if (real(random) < flame_intensity_drop)
                    flames[i].i--;
                if (real(random) < flame_float)
                    flames[i].y--;
            }

            if (flames[i].y <= 0 || flames[i].i <= 0) {
                // reset if particle dies or goes off screen
                flames[i].y = surface->h - 1;
                flames[i].i = 0;
            }
        } else {
            if (real(random) < flame_chance)
                flames[i].i = nflame_colors - 1;
        }

        // move randomly left and right
        if (real(random) < particle_wiggle)
            flames[i].x += real(random) < wind_direction ? -1 : 1;
        flames[i].x = modulo(flames[i].x, surface->w);

        // draw flame particle
        pixels[flames[i].x + flames[i].y * surface->w] = flame_color_table[flames[i].i];
    }
}

int main(int argc, char **argv) {
    SDL_Window *window = nullptr;
    SDL_Renderer *renderer = nullptr;

    if (SDL_Init(SDL_INIT_VIDEO) != 0) {
        std::cout << "Can't initialize SDL: " << SDL_GetError() << std::endl;
        cleanup(window, renderer);
        return EXIT_FAILURE;
    }

    window = SDL_CreateWindow(("rendering engine number "s + std::to_string(random())).c_str(), SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED,
                              DEFAULT_WINDOW_WIDTH, DEFAULT_WINDOW_HEIGHT, SDL_WINDOW_SHOWN | SDL_WINDOW_RESIZABLE);
    if (window == NULL) {
        std::cout << "Can't create window: " << SDL_GetError() << std::endl;
        cleanup(window, renderer);
        return EXIT_FAILURE;
    }

    renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC);
    if (renderer == NULL) {
        std::cout << "Can't create renderer: " << SDL_GetError() << std::endl;
        cleanup(window, renderer);
        return EXIT_FAILURE;
    }

    SDL_RendererInfo info;
    if (SDL_GetRendererInfo(renderer, &info) != 0) {
        std::cout << "renderer info failed: " << SDL_GetError() << std::endl;
        cleanup(window, renderer);
        return EXIT_FAILURE;
    }
    std::printf("renderer info\n\tname: %s\n\tflags: %d\n\ttexture formats (%u):\n", info.name, info.flags, info.num_texture_formats);
    for (size_t i = 0; i < info.num_texture_formats; i++)
        std::printf("\t\t%s\n", SDL_GetPixelFormatName(info.texture_formats[i]));
    std::printf("\tmax texture size: %d x %d\n", info.max_texture_width, info.max_texture_height);

    SDL_Texture *fire_texture = SDL_CreateTexture(renderer, SDL_PIXELFORMAT_ARGB8888, SDL_TEXTUREACCESS_STREAMING, 128, 64);
    SDL_Surface *surface;
    SDL_LockTextureToSurface(fire_texture, NULL, &surface);
    init_fire(surface);
    SDL_UnlockTexture(fire_texture);

    bool running = true;
    while (running) {
        SDL_SetRenderDrawColor(renderer, 0x00, 0x00, 0x00, SDL_ALPHA_OPAQUE);
        SDL_RenderClear(renderer);
        SDL_RenderCopy(renderer, fire_texture, NULL, NULL);
        SDL_RenderPresent(renderer);

        SDL_Event event;
        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_QUIT)
                running = false;
            if (event.type == SDL_KEYDOWN) {
                switch (event.key.keysym.sym) { ; }
            }
        }

        // const uint8_t *keys = SDL_GetKeyboardState(NULL);

        SDL_LockTextureToSurface(fire_texture, NULL, &surface);
        fire_effect(surface);
        SDL_UnlockTexture(fire_texture);
    }

    cleanup(window, renderer);
    return 0;
}