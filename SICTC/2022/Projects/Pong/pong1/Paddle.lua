Paddle = Class{}

-- Constructor
function Paddle:init(x,y,width,height,ai,type)
    self.x = x
    self.y = y
    self.type = type
    self.w = width
    self.h = height
    self.ai = ai
    if self.type == "hor" then
        self.dx = 0
    else
        self.dy = 0
    end
    self.score = START_SCORE
    self.ele = false
end

-- Update
function Paddle:update(dt)
    if ele then
        return
    end
    if self.type == "vert" then        
        if self.dy < 0 then
            self.y = math.max(0, self.y + self.dy * dt)
        else
            self.y = math.min(VIRTUAL_HEIGHT-self.h,self.y + self.dy * dt)
        end
    else
        if self.dx < 0 then
            self.x = math.max(0, self.x + self.dx * dt)
        else
            self.x = math.min(VIRTUAL_WIDTH-self.w,self.x + self.dx * dt)
        end 
    end
    if self.ai and self.type == "vert" then
        self.y = ball.y-self.h/2
    elseif self.ai and self.type == "hor" then
        self.x = ball.x-self.w/2
    end
end

function Paddle:removeScore()
    self.score = self.score-1
    if self.score < 1 then
        self.ele = true
    end
    if player1.ele and player2.ele and player3.ele then
        winner="player4"
        gameStateChange()
    elseif player4.ele and player1.ele and player2.ele then
        winner="player3"
        gameStateChange()
    elseif player3.ele and player4.ele and player1.ele then
        winner="player2"
        gameStateChange()
    elseif player3.ele and player4.ele and player2.ele then
        winner="player1"
    end
    if not winner == false then
        gameReset()
    end
end

-- Draw or render
function Paddle:render()
    if not self.ele then
        love.graphics.rectangle('fill',self.x,self.y,self.w,self.h)
    end
end