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
	db.collection("訂單").doc("測試訂單").set({
		品名:"測試",
		訂購網站:"測試",
		價格:"測試"
	})
}

function getdata() {
  var docRef = db.collection("movies").doc("新世紀福爾摩斯");
  docRef.get().then(function(doc) {
      if (doc.exists) {
        console.log(doc.data());
      } else {
        console.log("找不到文件");
      }
    })
    .catch(function(error) {
      console.log("提取文件時出錯:", error);
    });
}

//let scope= document.getElementById('search');
//scope.addEventListener('click', function()
//{
//	storedata();
//	alert('正在傳輸');
//});

let block1_trigger = document.getElementById('small_menu_unite1');
let block2_trigger = document.getElementById('small_menu_unite2');
let word_frame1 = document.getElementById('main_word_frame1');
let word_frame2 = document.getElementById('main_word_frame2');
block1_trigger.addEventListener('click', function()
{
	word1.style.color = '#FF9224';
	word2.style.color = '#000000';
	block1_trigger.style.cssText = 'border-bottom-style:outset;';
	block2_trigger.style.cssText  = 'border-bottom-style:none;';
	word_frame1.style.cssText  = 'display:flex';
	word_frame2.style.cssText  = 'display:none';
});

block2_trigger.addEventListener('click', function()
{
	word1.style.color = '#000000';
	word2.style.color = '#FF9224';
	block1_trigger.style.cssText  = 'border-bottom-style:none;';
	block2_trigger.style.cssText  = 'border-bottom-style:outset;';
	word_frame1.style.cssText  = 'display:none';
	word_frame2.style.cssText  = 'display:flex';
});

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

let basket_number=0;
let myButton = document.getElementById('myButton');
myButton.addEventListener('click', function(){
	
	basket_number=basket_number+1;
	localStorage.setItem('uid',basket_number);
	storedata();
	alert(basket_number);
});
