def longest_common_prefix(strs):
    if not strs:
        return ""
    if len(strs) == 1:
        return strs[0]
    common_prefix = ''
    first_string=strs[0]
    
    for i in range(len(first_string)):
        char = first_string[i]
        for string in strs[1:]:
            if i >= len(string) or string[i] != char:
                return common_prefix
        common_prefix += char
    return common_prefix
    
if __name__ == "__main__":  
    strings = ["flower", "flow", "flight"]
    result = longest_common_prefix(strings)
    print(f"The longest common prefix is: '{result}'")
