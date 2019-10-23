function mmarks(){
    var maths1=document.getElementById('maths').value;
    
    if(maths1>100||maths1<0){
    window.alert('Invalid Maths marks');
    }
    else if(maths1>=90)
    {document.getElementById('outa').innerHTML="S+";
    m1=10;}
    else if(maths1>=80){
    document.getElementById('outa').innerHTML="S";
    m1=9;}
    else if(maths1>=70)
    {document.getElementById('outa').innerHTML="A";
    m1=8;
}
    else if(maths1>=60){
    document.getElementById('outa').innerHTML="B";
    m1=7;}
    else if(maths1>=50){
    document.getElementById('outa').innerHTML="C";
    m1=6;}else{ 
    document.getElementById('outa').innerHTML="F";
    m1=5;}
    var ds1=document.getElementById('dsa').value;
   
    if(ds1>100||ds1<0)
    window.alert('Invalid DSA marks');

    else if(ds1>=90){
    document.getElementById('out').innerHTML="S+";
    d1=10;}
    else if(ds1>=80){
    document.getElementById('out').innerHTML="S";
    d1=9;}
    else if(ds1>=70){
    document.getElementById('out').innerHTML="A";
    d1=8;}
    else if(ds1>=60){
    document.getElementById('out').innerHTML="B";
    d1=7;}
    else if(ds1>=50){
    document.getElementById('out').innerHTML="C";
    d1=6;}
    else{ 
    document.getElementById('out').innerHTML="F";
    d1=5;}
    cgpa=(d1+m1)/2;
    document.getElementById('cgpa1').innerHTML=cgpa;
    }
