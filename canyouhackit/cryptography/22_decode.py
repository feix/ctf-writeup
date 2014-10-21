strtxt="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,./<>?;':[]{}=\+|-_()!@#$%^&*\""
stren="3e00c63d5596547df69235eac5389eb6138b4e6729af586dcbd9210a4c04b03107cf8e45240b5ad8e7a490713649aae65b3aef64a0beeb09f28c57ec8f741f0151989172613f69fe4bfa85fd146873260faccca14ddbab43461108b7"
strde="926d46434b1472851173433ed84b147285013efaa146434373fe68724685683ffafab714434daa"

txt2en = {}
for i in range(0, len(stren), 2):
    txt2en[stren[i:i+2]] = strtxt[len(strtxt)-1-i/2]

result = ""
for i in range(0, len(strde), 2):
    tmp = txt2en[strde[i:i+2]] 
    result = tmp + result

print(result)
