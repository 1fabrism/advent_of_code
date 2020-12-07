#include <iostream>
#include <vector>

int main()
{
    const int length = 5;
    int min_input = 172851;
    const int max_input = 675869;
    std::vector<int> result;
    for (int pwd = min_input; pwd <= max_input; ++pwd)
    {
        bool is_increasing = true;
        bool has_pair = false;
        bool repeats = false;
        bool reset = false;
        int counter = 1;
        int digits[length];
        int div = 1;
        for (int i = 0; i <= length; ++i)
        {
            // Isolate each digit to store them in an array:
            digits[i] = (pwd / div) % 10;
            div *= 10;

            // Check criteria:
            if (i && (digits[i] > digits[i - 1]))
            {
                is_increasing = false;
                break;
            }
            if (i && has_pair && (digits[i] != digits[i - 1]))
            {
                counter = 1;
                reset = true;
            }
            if (i && (digits[i] == digits[i - 1]))
            {
                ++counter;            
                if (counter == 2)
                {
                    has_pair = true;
                    repeats = false;
                }
                if ((counter > 2 && !reset) || (counter == 3 && reset && (i==5)))
                {
                    repeats = true;
                }
            }
        }

        if (is_increasing && has_pair && !repeats)
        {
            std::cout << pwd << std::endl;
            result.push_back(pwd);
        }
    }
    std::cout << size(result) << std::endl;
}
