//變數區
console.log("你好3");
/*
let word1 = document.getElementById('unite1_font');
let word2 = document.getElementById('unite2_font');

//firebase
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

firebase.initializeApp(firebaseConfig);
var db = firebase.firestore();

//let formal_input1 = document.getElementById('formal_input1');
//let formal_input2 = document.getElementById('formal_input2');
//let verification_input = document.getElementById('verification_input');
//let test_input = document.getElementById('test_input');

//function storedata() {
//    db.collection("帳號密碼").doc("用戶" + test_input.value + "的帳號密碼暫存").set({
//        帳號: formal_input1.value,
//        密碼: formal_input1.value,
//        驗證碼: verification_input.value
//    })
//}

//下載驗證碼圖片
let new_id = document.getElementById('new_id');
let picture = document.getElementById('picture');
console.log(new_id);
console.log(new_id.toString());
const fileRef = firebase.storage().ref("test");
fileRef.getDownloadURL().then(function(url) {
    picture.src = url;
})

//帳號密碼傳輸按鈕
let myButton = document.getElementById('myButton');
myButton.addEventListener('click', function() {
    if (formal_input1.value != "" & formal_input2.value != "" & verification_input.value != "" & test_input.value != "") {
        storedata();
        alert("資料傳輸成功");
    } else {
        alert("尚有欄位未填寫完畢");
    }
});
*/