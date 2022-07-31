import rhinoscriptsyntax as rs
texts = rs.GetObjects("Select texts", rs.filter.annotation)
for text in texts:
    crd = rs.TextObjectPoint(text)
    print crd

