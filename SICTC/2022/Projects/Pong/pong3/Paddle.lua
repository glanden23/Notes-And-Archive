Paddle = Class{}

-- Constructor
function Paddle:init(x,y,width,height,ai,type,player)
    self.x = x
    self.y = y
    self.type = type
    self.w = width
    self.h = height
    self.ai = ai
    self.player = player
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
    if self.ai then
        self:AI(dt)
    end
end

function Paddle:AI(dt)
    if self.player == "1" then
        if ball.x > VIRTUAL_WIDTH/2 then
            return
        end
    elseif self.player == "2" then
        if ball.x < VIRTUAL_WIDTH/2 then
            return
        end
    elseif self.player == "3" then
        if ball.y > VIRTUAL_HEIGHT/2 then
            return
        end
    elseif self.player == "4" then
        if ball.y < VIRTUAL_HEIGHT/2 then
            return
        end
    end
    if self.type == "hor" then
        if self.x > ball.x then
            self.x=self.x-(PADDLE_SPEED-35+love.math.random(-50,50))*dt
        else
            self.x=self.x+(PADDLE_SPEED-35+love.math.random(-50,50))*dt
        end
    else
        if self.y > ball.y then
            self.y=self.y-(PADDLE_SPEED-35+love.math.random(-50,50))*dt
        else
            self.y=self.y+(PADDLE_SPEED-35+love.math.random(-50,50))*dt
        end
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