--[[
    For each holographic projector:
        figure out what y-level it's on
            either makes its height static
            or make its height change based on time and distance
]]
function Update(I)
    local projectorCount = I:Component_GetCount(33)
    for i = 0, projectorCount, 1 do
        --Get the local position of a hologram projector
        local localPos = I:Component_GetLocalPosition(33, i)
        if localPos.y == 0 then
            I:Component_SetFloatLogic_1(33, i, 4, 10.0)
            --I:Log("Set ID#"..i.." to height=10.0")
        else
            local time = I:GetTime()
            local distancePercent = ((localPos.z+1.0)/100.0)
            local distancePercentOfPi = distancePercent*math.pi
            local height = 3.0*(math.cos(time-distancePercentOfPi))+7.0
            --[[ I:Log("time="..time)
            I:Log("distancePercent="..distancePercent)
            I:Log("distancePercentOfPi="..distancePercentOfPi)
            I:Log("height="..height) ]]
            I:Component_SetFloatLogic_1(33, i, 4, height)
            I:Log("Set ID#"..i.." to height="..height)
        end
    end
end