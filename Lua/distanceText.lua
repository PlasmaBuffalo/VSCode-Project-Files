function Update(I)
    local projectorCount = I:Component_GetCount(33)
    for i = 0, projectorCount, 1 do
        --Get the local position of a hologram projector
        local localPos = I:Component_GetLocalPosition(33, i)
        --I:Log("LP-Vector="..localPos.x..", "..localPos.y..", "..localPos.z)
        --Get the magnitude of the vector relative to our origin point (in this case, z-axis)
        local blockDist = localPos.z + 1
        --I:Log("ID#"..i.." distance="..blockDist)
        I:Component_SetFloatLogic_1(33, i, 4, blockDist)
    end
end
