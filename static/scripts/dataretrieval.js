"use strict";

document.addEventListener('DOMContentLoaded', initPage, false);

function initPage() {
	// initially, show the root albumId
	retrieveAndDisplayImages(0);
}

function retrieveAndDisplayImages(albumId) {
	// remove any existing images
	var existingItems = document.querySelectorAll(".albumImageContainer .item");
	var count;
	console.log(existingItems.length);
	for (count=0; count<existingItems.length; count++) {
		existingItems[count].parentNode.removeChild( existingItems[count] );
	}
	
	// display spinner
	var spinner = document.querySelector(".albumImageContainer .loading");
	spinner.style.display = "block";
	
	// fetch image data for given albumId and dispatch to callback method
	var xhr = new XMLHttpRequest();
	xhr.open('POST', 'getImages');
	xhr.setRequestHeader('Content-Type', 'application/json');
	xhr.onload = function() {
		if (xhr.status === 200) {
			displayImages(xhr.responseText);
		}
		else {
			console.log("error");
		}
		hideSpinner();
	};
	xhr.send(JSON.stringify({
		albumId: albumId
	}));
}



function displayImages(responseText) {
	var data = JSON.parse(responseText);
	var count;
	var container = document.querySelector('.albumImageContainer');
	for(count=0;count<data.length;count++) {
		var commentCount = data[count].commentCount;
		var fileName = data[count].fileName;
		
		var markUp = '<div class="item"> \
				<div class="imageContainer"> \
					<img src="'+fileName+'" alt="" data-jslghtbx data-jslghtbx-group="mygroup1" data-jslghtbx-caption="number of comments: '+commentCount+'"> \
				</div> \
				<div class="controls"> \
					<span>Comment</span> \
				</div> \
			</div>';
		
		container.insertAdjacentHTML('beforeend', markUp);
	}
	lightbox.load();
}

function hideSpinner() {
	var spinner = document.querySelector(".albumImageContainer .loading");
	spinner.style.display = "none";
}
