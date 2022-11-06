Paddle = Class{}

-- Constructor
function Paddle:init(x,y,width,height)
    self.x = x
    self.y = y
    self.w = width
    self.h = height
    self.dy = 0
    self.score = 0
end

-- Update
function Paddle:update(dt)
    if self.dy < 0 then
        self.y = math.max(0, self.y + self.dy * dt)
    else
        self.y = math.min(VIRTUAL_HEIGHT-self.h,self.y + self.dy * dt)
    end
end

function Paddle:addScore()
    self.score = self.score+1
end

-- Draw or render
function Paddle:render()
    love.graphics.rectangle('fill',self.x,self.y,self.w,self.h)
end