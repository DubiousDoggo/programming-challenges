#include <deque>

class teque
{

    std::deque<int> head;
    std::deque<int> tail;

public:

    void balance()
    {
        while (head.size() - 1 > tail.size())
        {
            tail.push_front(head.back());
            head.pop_back();
        }
        while (head.size() < tail.size())
        {
            head.push_back(tail.front());
            tail.pop_front();
        }
    }

    size_t size()
    {
        return head.size() + tail.size();
    }

    int &operator[](size_t i)
    {
        if (i < head.size())
            return head[i];
        else
            return tail[i - head.size()];
    }

    void push_back(int x)
    {
        tail.push_back(x);
    }

    void push_front(int x)
    {
        head.push_front(x);
    }

    void push_middle(int x)
    {
        balance();
        head.push_back(x);
    }
};

#include <cstdio>
#include <cstring>

int main()
{
    teque tq;
    unsigned n;
    char s[16];
    int x;
    std::scanf("%u", &n);
    for (unsigned i = 0; i < n; i++)
    {
        std::scanf("%s %u", s, &x);
        if (std::strcmp(s, "push_back") == 0)
            tq.push_back(x);
        else if (std::strcmp(s, "push_front") == 0)
            tq.push_front(x);
        else if (std::strcmp(s, "push_middle") == 0)
            tq.push_middle(x);
        else if (std::strcmp(s, "get") == 0)
            std::printf("%u\n", tq[x]);
    }
    return 0;
}
