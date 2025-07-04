def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix
if __name__ == "__main__":  
    strings = ["flower", "flow", "flight"]
    result = longest_common_prefix(strings)
    print(f"The longest common prefix is: '{result}'")