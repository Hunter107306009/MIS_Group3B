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

//let scope= document.getElementById('search');
//scope.addEventListener('click', function()
//{
//	storedata();
//	alert('正在傳輸');
//});


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