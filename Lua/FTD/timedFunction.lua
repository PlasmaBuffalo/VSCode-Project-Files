-- after an indicated period of time passes, the function will be called again
-- amount of time to take between function calls (in seconds)
local loopInterval = 10

function Timer(I)
    -- get the current time
    local time = Mathf.Floor(I:GetTime() % loopInterval)
    -- whenever time is zero, return true
    if time == 0 then
        return true
    else
        return false
    end -- close if statement
end -- close function