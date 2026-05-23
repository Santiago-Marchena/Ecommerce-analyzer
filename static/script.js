const form =
document.getElementById(
"productForm"
)

form.addEventListener(

"submit",

async(e)=>{

e.preventDefault()

const response=
await fetch(

"/product/analyze",

{

method:"POST",

headers:{

"Content-Type":
"application/json"

},

body:

JSON.stringify({

name:
document
.getElementById(
"name"
).value,

cost:
Number(
document
.getElementById(
"cost"
).value
),

price:
Number(
document
.getElementById(
"price"
).value
),

competition:
document
.getElementById(
"competition"
).value,

demand:
document
.getElementById(
"demand"
).value,

shipping_days:
Number(
document
.getElementById(
"shipping"
).value
)

})

}

)

const data=
await response.json()

document
.getElementById(
"margin"
)

.innerHTML=

data.margin


document
.getElementById(
"score"
)

.innerHTML=

data.score


let riskText=""

if(
data.risk==="low"
){

riskText="Bajo"

}

else if(
data.risk==="medium"
){

riskText="Medio"

}

else{

riskText="Alto"

}

document
.getElementById(
"risk"
)

.innerHTML=

riskText


let text=""

if(
data.score>=80
){

text=
"✅ Producto altamente recomendable"

}

else if(
data.score>=60
){

text=
"⚠️ Producto viable con monitoreo"

}

else{

text=
"❌ Producto con riesgo elevado"

}

document
.getElementById(
"recommendation"
)

.innerHTML=

"<strong>Recomendación</strong><br><br>"

+

text

})