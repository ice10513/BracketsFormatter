import sys

class BracketContextData:
    def __init__(self, p_indent):
        self.indent = p_indent

class BracketContextDataStack:
    def __init__(self):
        self.bracketContextDatas = []
    
    def push(self):
        if len(self.bracketContextDatas) == 0:
            l_data = BracketContextData(4)
        else:
            l_data = BracketContextData(self.top().indent + 4)

        self.bracketContextDatas.append(l_data)

    def pop(self):
        return self.bracketContextDatas.pop()

    def top(self):
        return self.bracketContextDatas[-1]
    
    def clear(self):
        self.bracketContextDatas.clear()

    def lastIndent(self):
        return self.top().indent - 4
    
    def nextIndent(self):
        return self.top().indent + 4
    
    def currentIndent(self):
        return self.top().indent

class BracketsFormatter:
    def __init__(self):
        self.bracketContextDataStack = BracketContextDataStack()

    def format(self, p_rawData):
        self.bracketContextDataStack.clear()

        l_str = ''
        for l_ch in p_rawData:
            if l_ch == '<':
                self.bracketContextDataStack.push()

                print(' ' * self.bracketContextDataStack.lastIndent() + l_str.strip())
                print(' ' * self.bracketContextDataStack.lastIndent() + '<')
                l_str = ''
    
            elif l_ch == '>':
                print(' ' * self.bracketContextDataStack.currentIndent() + l_str.strip())
                print(' ' * self.bracketContextDataStack.lastIndent() + '>')
                l_str = ''

                self.bracketContextDataStack.pop()
            
            elif l_ch == ',':
                l_str += l_ch
                print(' ' * self.bracketContextDataStack.currentIndent() + l_str.strip())
                l_str = ''
            else:
                l_str += l_ch

if __name__ == '__main__':

    if len(sys.argv) == 1:
        print('command: BracketsFormatter template string')
        exit('0') 

    l_formatter = BracketsFormatter()
    l_formatter.format(sys.argv[1])
    # l_formatter.format('template <typename T, typename U, template<typename, typename> class Container>')
    # l_formatter.format('const std::basic_string<char, std::char_traits<char>, std::allocator<char> >')
    # l_formatter.format('std::unordered_map<std::vector<std::map<std::pair<char, double>, int>>, std::list<std::tuple<unsigned, bool, float>>>')