const adRnd = Math.random();
let provider = (adRnd < 0.95 ? "sparteo" : "google");
let pageType = "";

const uic_prov_pre = (pt, provParam, subjectFolder) => {
  if (pt == "default" || pt == "landing" || pt == "tryit" || pt == "tryitdb" || pt == "exercise" || pt == "xrcise" || pt == "video" || pt == "explainer" ) { pageType = pt; }
  if (pageType == "video" || pageType == "explainer" ) { provider = "sparteo"; }
  if (provParam == "snigel" || provParam == "sparteo" || provParam == "google") { provider = provParam; }
  if (!_uic_u_ok()) {
    if (pageType != "landing") {
      if (provider == "sparteo") {
        window._hbdbrk = window._hbdbrk || [];
        window._hbdbrk.push([
          "_vars",
          { page_type: pageType, custom1: subjectFolder, custom5: "unknown"}
        ]);
      } else if (provider == "google") {
        window.googletag = window.googletag || {cmd: []};
        if (pageType == "default") {
          googletag.cmd.push(function() {
            let leaderMapping = googletag.sizeMapping().addSize([0, 0], [[320, 50], [300, 250]] ).addSize([512, 0], [[320, 50], [300, 250]]).addSize([774, 0], [[320, 50], [468, 60], [300, 250], [728, 90]]).addSize([993, 0], [[320, 50], [468, 60]]).addSize([1176, 0], [[320, 50], [468, 60], [728, 90]]).addSize([1465, 0], [[320, 50], [468, 60], [300, 250], [728, 90], [970, 90], [970, 250]]).build();
            googletag.defineSlot('/16833175/MainLeaderboard', [[320, 50], [468, 60], [728, 90], [970, 90]], 'div-gpt-ad-1422003450156-2').defineSizeMapping(leaderMapping).addService(googletag.pubads());
            let stickyMapping = googletag.sizeMapping().addSize([0, 0], []).addSize([992, 0], [120, 600]).addSize([1261, 0], [[120, 600], [160, 600]]).addSize([1701, 0], [[120, 600], [160, 600],  [300, 600], [300, 1050]]).build();
            googletag.defineSlot('/16833175/StickySkyScraper', [[120, 600], [160, 600], [300, 600], [300, 1050]], 'div-gpt-ad-1472547360578-0').defineSizeMapping(stickyMapping).addService(googletag.pubads());
            let mcontMapping = googletag.sizeMapping().addSize([0, 0], [[320, 50], [300, 250]] ).addSize([512, 0], [[320, 50], [300, 250]]).addSize([774, 0], [[320, 50], [468, 60], [300, 250], [728, 90]]).addSize([993, 0], [[320, 50], [468, 60]]).addSize([1176, 0], [[320, 50], [468, 60], [728, 90]]).addSize([1465, 0], [[320, 50], [468, 60], [300, 250], [728, 90], [970, 90], [970, 250]]).build();
            googletag.defineSlot('/16833175/MidContent', [[300, 250], [336, 280], [320, 50], [468, 60], [728, 90], [970, 90]], 'div-gpt-ad-1493883843099-0').defineSizeMapping(mcontMapping).setCollapseEmptyDiv(true).addService(googletag.pubads());
            googletag.pubads().enableSingleRequest();
            googletag.pubads().setTargeting('page_section', subjectFolder);
            googletag.pubads().disableInitialLoad();
            googletag.pubads().setCentering(true);
          });
        } else if (pageType == "exercise" || pageType == "xrcise") {
          googletag.cmd.push(function() {
            let leaderMapping = googletag.sizeMapping().addSize([0, 0], [320, 50]).addSize([468, 0], [[320, 50], [468, 60]]).addSize([728, 0], [[320, 50], [468, 60], [728, 90]]).addSize([970, 0], [[320, 50], [468, 60], [728, 90], [970, 90]]).build();
            googletag.defineSlot('/16833175/TryitLeaderboard', [[320, 50], [468, 60], [728, 90], [970, 90]], 'div-gpt-ad-1428407818244-0').defineSizeMapping(leaderMapping).addService(googletag.pubads());
            googletag.pubads().enableSingleRequest();
            googletag.pubads().setTargeting('page_section', subjectFolder);
            googletag.pubads().disableInitialLoad();
            googletag.pubads().setCentering(true);
          });
        } else if (pageType == "tryitdb" || pageType == "tryit") {
          googletag.cmd.push(function() {
            let leaderMapping = googletag.sizeMapping().addSize([0, 0], [320, 50]).addSize([468, 0], [[320, 50], [468, 60]]).addSize([728, 0], [[320, 50], [468, 60], [728, 90]]).addSize([970, 0], [[320, 50], [468, 60], [728, 90], [970, 90]]).build();
            googletag.defineSlot('/16833175/TryitLeaderboard', [[320, 50], [468, 60], [728, 90], [970, 90]], 'div-gpt-ad-1428407818244-0').defineSizeMapping(leaderMapping).addService(googletag.pubads());
            let stickyMapping = googletag.sizeMapping().addSize([0, 0], []).addSize([992, 0], [[120, 600], [160, 600]]).addSize([1820, 0], [160, 600]).addSize([1683, 0], [[120, 600], [160, 600], [300, 250], [300, 600], [300, 1050]]).build();
            googletag.defineSlot('/16833175/StickySkyScraper', [[120, 600], [160, 600], [300, 250], [300, 600], [300, 1050]], 'div-gpt-ad-1472547360578-0').defineSizeMapping(stickyMapping).addService(googletag.pubads());
            googletag.pubads().enableSingleRequest();
            googletag.pubads().setTargeting('page_section', subjectFolder);
            googletag.pubads().disableInitialLoad();
            googletag.pubads().setCentering(true);
          });
        }
      }
    }
  } else if (_uic_u_ok()) {
    if (pageType == "video") {
      window._hbdbrk = window._hbdbrk || [];
      window._hbdbrk.push([
        "_vars",
        { page_type: pageType, custom1: subjectFolder, custom5: "premium" }
      ]);
    }
  }
  if ( (!_uic_u_ok() && (pageType != "landing")) || (_uic_u_ok() && (pageType == "video"))) {
    (function(){
    const provLoader=document.createElement('script');
    provLoader.type='text/javascript';
    if (provider == "sparteo") {
      provLoader.async=true;
      provLoader.setAttribute("data-cfasync", "false");
      provLoader.src='https://www.flashb.id/universal/55f786fc-6e0e-5368-ade6-451e5d54251d.js';
    } else if ( provider == "snigel") {
      provLoader.async=true;
      provLoader.src='https://cdn.snigelweb.com/adengine/w3schools.com/loader.js';
    } else if ( provider == "google") {
      provLoader.async=true;
      provLoader.src='https://securepubads.g.doubleclick.net/tag/js/gpt.js';
      provLoader.setAttribute("crossorigin", "anonymous");
    }
    (document.getElementsByTagName('head')[0]||document.getElementsByTagName('body')[0]).appendChild(provLoader);
    })();
  }
}

const uic_prov_sec = () => {
  if (!_uic_u_ok()) {
    if (provider == "sparteo" && (pageType == "default" || pageType == "video")) {
      window.addEventListener("scroll", fix_stickyad);
      window.addEventListener("resize", fix_stickyad);
    } else {
      if (pageType == "default" || pageType == "video") {
        const mainHeight = Number(w3_getStyleValue(document.getElementById("main"), "height").replace("px", ""));
        if (provider == "google") {
          const midAdElement = document.getElementById("div-gpt-ad-1493883843099-0");
          if (mainHeight > 2000) {
            if (midAdElement) {
              googletag.cmd.push(function () { googletag.display('div-gpt-ad-1493883843099-0'); });
              googletag.cmd.push(function () { googletag.display('div-gpt-ad-1472547360578-0'); });
            } else {
              googletag.cmd.push(function () { googletag.display('div-gpt-ad-1472547360578-0'); });
            }
          } else if (midAdElement) { 
            googletag.cmd.push(function () { googletag.display('div-gpt-ad-1493883843099-0'); });
          }
          googletag.enableServices();
          googletag.pubads().refresh();
        }
        window.addEventListener("scroll", fix_stickyad);
        window.addEventListener("resize", fix_stickyad);
      } else if (pageType == "tryitdb" || pageType == "tryit") {
        if (provider == "google") {
          googletag.cmd.push(function () { googletag.display('div-gpt-ad-1472547360578-0'); });
          googletag.enableServices();
          googletag.pubads().refresh();
        }
      } else if (pageType == "xrcise") {       
        if (provider == "google") {
          googletag.enableServices();
          googletag.pubads().refresh();
        }
      }
    }
  }
}

const uic_prov_al = () => {
  const mainLeaderboard = document.getElementById("mainLeaderboard");
  const midContent = document.getElementById("midcontentadcontainer");
  const wideSkyscraper = document.getElementById("skyscraper");
  const vidPos = document.getElementById("vidpos");
  const stickySkyscraper = document.getElementById("stickyadcontainer");
  const bottom = document.getElementById("bottomads");
  const tryitLeaderboard = document.getElementById("tryitLeaderboard");
  const sqlstickyadcontainer = document.getElementById("sqlstickyadcontainer");
  const bottomPlacement = document.getElementById("bottomad");
  const internalAd = document.getElementById("upperfeatureshowcaselink");
  const stickyPos = document.getElementById("stickypos");
  const xleftad = document.getElementById("xleftad");
  const xrightad = document.getElementById("xrightad");
  if (_uic_u_ok()) {
    if (pageType == "default" || pageType == "video" ) {
      if (mainLeaderboard) { mainLeaderboard.remove(); }
      if (midContent) {
        const previousSibling = midContent.previousElementSibling;
        if (previousSibling) { previousSibling.remove(); }
        midContent.remove();
      }
      const mainElement = document.getElementById("main");
      if (mainElement) {
        mainElement.classList.remove("l10");
        mainElement.classList.add("l12");
        mainElement.style.width = "100%";
        mainElement.style.borderRight = "none";
      }
      const rightElement = document.getElementById("right");
      if (rightElement) { rightElement.remove(); }
      if (bottom.length > 0) {
        const bottomAdParentElement = bottom[0].parentElement;
        if (bottomAdParentElement) {
          const previousElement = bottomAdParentElement.previousElementSibling;
          if (previousElement) { previousElement.remove(); }
          bottomAdParentElement.remove();
        }
      }
      if (typeof fix_stickyad === "function") { 
        window.removeEventListener("scroll", fix_stickyad);
        window.removeEventListener("resize", fix_stickyad);
      }
    } else if (pageType == "tryit") {
      if (tryitLeaderboard) { tryitLeaderboard.remove(); }
      const breadcrumb = document.getElementById("breadcrumb");
      const container = document.getElementById("container");
      const tryTopNav = document.getElementsByClassName("trytopnav");
      const dragBar = document.getElementById("dragbar");
      if (breadcrumb) {
        if (tryTopNav.length > 0) { tryTopNav[0].style.top = "40px"; }
        if (dragBar) { dragBar.style.top = "85px"; }
        if (container) { container.style.top = "85px"; }
      } else {
        if (container) {
          if (tryTopNav.length > 0) { tryTopNav[0].style.top = "0px"; }
          if (dragBar) { dragBar.style.top = "45px"; }
          container.style.top = "45px";
          container.style.setProperty("width", "calc(100%)", "important");
          tryTopNav[0].style.setProperty("width", "calc(100%)", "important");
        } else {
          const altContainer = document.getElementsByClassName("container");
          if (altContainer.length > 0) { altContainer[0].style.top = "0px"; }
        }
      }
    } else if (pageType == "tryitdb") {
      document.getElementById("tryitLeaderboard").remove();
      document.getElementById("sqlstickyadcontainer").remove();
    } else if (pageType == "xrcise") {
      document.getElementById("tryitLeaderboard").parentElement.parentElement.remove();
      document.getElementById("xleftad").remove();
      document.getElementById("xrightad").remove();
    } else if (pageType == "exercise") {
      if (tryitLeaderboard) { tryitLeaderboard.parentElement.parentElement.remove();}
      document.getElementById("menubtn").style.left = "";
      document.getElementById("menubtn").style.right = "20px";
      document.getElementById("assignmenttext").previousElementSibling.style.textAlign = "center";
      document.getElementById("assignmenttext").previousElementSibling.style.marginTop = "0";
      document.getElementById("assignmenttext").previousElementSibling.style.paddingTop = "0";
      document.getElementById("menubtn").style.top = "40px";
    }
  } else {
    if (pageType == "default" || pageType == "video") {
      (function(){
        let provLeaderboard=document.createElement('div');
        if (provider == "google") {
          provLeaderboard.id='div-gpt-ad-1422003450156-2';
        }
        if (mainLeaderboard) {
          mainLeaderboard.appendChild(provLeaderboard);
          if (provider == "google") { googletag.cmd.push(function () { googletag.display('div-gpt-ad-1422003450156-2'); });}
        }
      })();
      (function(){
        let provMidContent=document.createElement('div');
        if (provider == "google") {
          provMidContent.id='div-gpt-ad-1493883843099-0';
          provMidContent.style='display: inline-block;';
        }
        if (midContent) {
          midContent.appendChild(provMidContent); 
          (function () {
            let removeAdContainer = document.createElement('p');
            removeAdContainer.className = 'remove-ads-container';
            let removeAdLink = document.createElement('a');
            removeAdLink.className = 'remove-ads ga-featured ga-remove-ads';
            removeAdLink.href = 'https://order.w3schools.com/plans';
            removeAdLink.target = '_blank';
            removeAdLink.rel = 'noopener';
            removeAdLink.textContent = 'REMOVE ADS';
            removeAdContainer.appendChild(removeAdLink);
            midContent.appendChild(removeAdContainer);
          })();       
        }
      })();
      (function(){
        let provStickySky=document.createElement('div');
        if (provider == "google") {
          provStickySky.id='div-gpt-ad-1472547360578-0';
        }
        if (stickySkyscraper && stickySkyscraper.style.display != "none") {
          stickySkyscraper.children[0].appendChild(provStickySky);
        } else {
          stickySkyscraper.remove();
          if (typeof fix_stickyad === "function") { 
            window.removeEventListener("scroll", fix_stickyad);
            window.removeEventListener("resize", fix_stickyad);
          }
        }
      })();
    } else if (pageType == "tryit" || pageType == "xrcise" || pageType == "exercise" || pageType == "tryitdb" ) {
      if (provider=="google") {
        if (pageType == "xrcise") { document.getElementById("exercise_main_leaderboard").style.setProperty('display', 'block', 'important'); }
        if (pageType == "tryit" || pageType == "exercise") { document.getElementById("tryitLeaderboard").style.setProperty('display', 'block', 'important'); }
      }
      let mainWidth = "0";
      (function(){
        let provLeaderboard=document.createElement('div');
        if (provider == "google" && pageType == "tryit") {
          mainWidth = Number(w3_getStyleValue(document.getElementsByTagName("body")[0], "width").replace("px", ""));
          if (mainWidth > 1008) {
            let provDBSky=document.createElement('div');
            tryitLeaderboard.style.height="0";
            provDBSky.id='div-gpt-ad-1472547360578-0';
            provDBSky.style = "width: 240px; height: 100%; background-color: #FFF; right: 10px; float:right; padding: 4px; box-sizing: border-box;";
            if (document.getElementById("container")) { document.getElementById("container").after(provDBSky); }
          } else {
            provLeaderboard.id='div-gpt-ad-1428407818244-0';
            tryitLeaderboard.style.height="90px";
            if (tryitLeaderboard) { tryitLeaderboard.appendChild(provLeaderboard); }
          }      
        } else {
          provLeaderboard.id='div-gpt-ad-1428407818244-0';
          if (tryitLeaderboard) { tryitLeaderboard.appendChild(provLeaderboard); }
        }
      })();
      if (pageType == "tryitdb") {
        (function(){
          let provDBSky=document.createElement('div');
          if (provider == "google") {
            provDBSky.id='div-gpt-ad-1472547360578-0';
          }
          if (sqlstickyadcontainer) { sqlstickyadcontainer.appendChild(provDBSky); }
        })();
      }
      if (provider == "google") {
        if (pageType == "tryit" && mainWidth > 1008) {
          googletag.cmd.push(function () { googletag.display('div-gpt-ad-1472547360578-0'); });
        } else {
          googletag.cmd.push(function () { googletag.display('div-gpt-ad-1428407818244-0'); });
        }
      } 
    }
    docReady(function() {
      let checkReadyState = setInterval(function () {
        if (document.readyState === "interactive" || document.readyState === "complete") {
          clearInterval(checkReadyState);
          // Ensure FastCMP (__tcfapi) is loaded and CMP is ready before running uic_prov_sec
          let checkFastCmp = setInterval(function () {
            if (typeof window.__tcfapi !== "function") {
              return;
            }
            window.__tcfapi('ping', 2, function (res, success) {
              if (!success || !res) {
                return;
              }
              if (res.cmpLoaded && res.cmpStatus !== 'stub') {
                clearInterval(checkFastCmp);
                uic_prov_sec();
              }
            });
          }, 300); // check every 300ms
        }
      }, 300); // check every 300ms
    });

  }
}

const uic_prov_run = () => {
  if (!_uic_u_ok()) {
    const sqlstickyadcontainer = document.getElementById("sqlstickyadcontainer");
    if (pageType == "tryit" || pageType == "exercise" || pageType == "tryitdb" ) {
      if (provider == "google") {
        googletag.cmd.push(function () { googletag.display('div-gpt-ad-1428407818244-0'); });
        googletag.pubads().refresh();
      }
      if (sqlstickyadcontainer) {
        if (provider == "google") {
          googletag.cmd.push(function () { googletag.display('div-gpt-ad-1472547360578-0'); });
          googletag.pubads().refresh();
        }
      }
    }
  }
}