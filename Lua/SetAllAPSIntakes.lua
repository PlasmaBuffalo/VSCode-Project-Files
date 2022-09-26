--sets every ammo intake on a craft to use a given ammo controller
function Update(I)
    --get the ID of the controller to apply to the intakes
    local acID = 11
    --find the APS intake count(component ID of intake = 20)
    local intakeCount = I:Component_GetCount(20)
    --loop through each intake assumming standard indexing
    for blockIndex = 0, intakeCount, 1 do
        --for each intake, set ammo controller to acID
        I:Log("setting index#"..blockIndex)
        I:Component_SetIntLogic_1(20, blockIndex, 0, acID)
    end
end