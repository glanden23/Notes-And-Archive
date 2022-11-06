function tablelen(T)
    local c = 0
    for _ in pairs(T) do c = c + 1 end
    return c
end