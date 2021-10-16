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

let count=0;
let block_1 = document.getElementById('block_1');
let block_2 = document.getElementById('block_2');
block_1.addEventListener('click', function(){

	count=count+1;

	if (count%2==0){
		block_1.style.cssText  = 'background-color:#EA7500; color:#FCFCFC;';
		block_2.style.cssText  = 'background-color:#E0E0E0; color:#3C3C3C;';
	}

	if (count%2==1){
		block_1.style.cssText  = 'background-color:#E0E0E0; color:#3C3C3C;';
		block_2.style.cssText  = 'background-color:#EA7500; color:#FCFCFC;';
	}

});

block_2.addEventListener('click', function(){

	count=count+1;

	if (count%2==0){
		block_1.style.cssText  = 'background-color:#EA7500; color:#FCFCFC;';
		block_2.style.cssText  = 'background-color:#E0E0E0; color:#3C3C3C;';
	}

	if (count%2==1){
		block_1.style.cssText  = 'background-color:#E0E0E0; color:#3C3C3C;';
		block_2.style.cssText  = 'background-color:#EA7500; color:#FCFCFC;';
	}

});