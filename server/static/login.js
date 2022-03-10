let burger=document.getElementsByClassName('burger')[0]
let links=document.getElementsByClassName('links')[0]
let eid=document.getElementById('i1')
let pwd=document.getElementById('i2')
let sb=document.getElementsByTagName('button')[0]
burger.addEventListener('click',()=>
{
    links.classList.toggle('active_link')
})

sb.addEventListener('click',()=>
{
    if (pwd.value.length==0 || eid.value.length==0)
    alert("fill the fields properly")
})