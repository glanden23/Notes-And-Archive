-- comment
--[[
    Multiline
    comment
]]
hello = 'hello'
local test = "local"

function say(text)
    print(text)
end

say(hello .. test)

local i = 10
while i>0 do
    i = i-1
    print(i)
end

for j=10,0,-1 do
    print()
end

i = 10
repeat
    i=i-1
    print(i)
until i==0

--Tables
--Glorified list
-- Java and C call this hash map
-- Python calls it a Dictionary
local person = {}
person.name="Bander"
person.age=75
person.height=7.0
print(person['name'])