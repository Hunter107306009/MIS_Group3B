//記得註釋

//變數區
let word1 = document.getElementById('unite1_font');
let word2 = document.getElementById('unite2_font');

var firebaseConfig = {
    apiKey: "AIzaSyD7tE_NRFk7SenBFUkUCH3WgFdaKQcX304",
    authDomain: "test-4fa88.firebaseapp.com",
    databaseURL: "https://test-4fa88-default-rtdb.asia-southeast1.firebasedatabase.app",
    projectId: "test-4fa88",
    storageBucket: "test-4fa88.appspot.com",
    messagingSenderId: "951903532283",
    appId: "1:951903532283:web:7d9c1c38cd632fb471ac5e",
    measurementId: "G-NSP6DRS2MS"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);

var db=firebase.firestore();

function storedata(){
	db.collection("訂單").doc("蝦仁訂單").set({
		品名:"美式賣場熱銷帶尾特大無毒割背蝦仁800克",
		訂購網站:"熊媽媽買菜網",
		價格:"990元"
	})
}

//選單彈出
let undo = document.getElementById('undo');
let side_menu = document.getElementById('side-menu');
let side_paste = document.getElementById('side-paste');
let click_count = 0;
undo.addEventListener('click', function()
{
	if (click_count%2==0){
		side_menu.style.cssText  = 'display:flex';
		side_paste.style.cssText  = 'display:flex';
	}
	
	if (click_count%2==1){
		side_menu.style.cssText  = 'display:none';
		side_paste.style.cssText  = 'display:none';
	}

	click_count=click_count+1;
});

//交換動畫
let haed_2 = document.getElementById('haed_2');
let haed_3 = document.getElementById('haed_3');
for(i=1;i<($(".small_menu_frame").length);i++){
    (function(x) {
        document.getElementById('body'+x.toString()+'_1').addEventListener('click', function()
        {
            var T_haed_2=haed_2.textContent;
            var T_haed_3=haed_3.textContent;
            haed_2.textContent=document.getElementById('body'+x.toString()+'_2').textContent;
            haed_3.textContent=document.getElementById('body'+x.toString()+'_3').textContent;
            document.getElementById('body'+x.toString()+'_2').textContent=T_haed_2;
            document.getElementById('body'+x.toString()+'_3').textContent=T_haed_3;
        });
    })(i)
}