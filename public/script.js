document.getElementById('year').textContent=new Date().getFullYear();
document.addEventListener('DOMContentLoaded',()=>{
  const locale=document.documentElement.dataset.pageLang||'no';
  const copy={
    no:{choose:'Velg denne løsningen',desired:'Ønsket løsning',placeholder:'For eksempel matt tak med lyslinjer',sending:'Sender forespørselen…'},
    en:{choose:'Choose this solution',desired:'Preferred solution',placeholder:'For example, a matte ceiling with light lines',sending:'Sending your enquiry…'},
    uk:{choose:'Обрати це рішення',desired:'Бажане рішення',placeholder:'Наприклад, матова стеля зі світловими лініями',sending:'Надсилаємо заявку…'}
  }[locale];
  const form=document.getElementById('contactForm');
  const dialog=document.querySelector('.solution-dialog');
  if(!form)return;
  const selection=form.querySelector('#desired-solution');
  if(dialog){
    const choose=document.createElement('button');
    choose.type='button';choose.className='btn primary solution-dialog-choose';
    choose.textContent=copy.choose;
    const actions=document.createElement('div');
    actions.className='solution-dialog-actions';
    actions.append(choose);
    dialog.querySelector('.solution-dialog-back').append(actions);
    choose.addEventListener('click',()=>{
      const title=dialog.querySelector('#solution-dialog-title').textContent;
      const choices=selection.value.split(';').map(value=>value.trim()).filter(Boolean);
      if(!choices.includes(title))choices.push(title);
      selection.value=choices.join('; ');
      dialog.querySelector('.solution-dialog-close').click();
      setTimeout(()=>{
        selection.focus({preventScroll:true});
        selection.scrollIntoView({block:'center',behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth'});
      },matchMedia('(prefers-reduced-motion: reduce)').matches?0:1250);
    });
  }
  // Keep the native POST and redirect; reject repeated activation while it is pending.
  let submitting=false;
  const submit=form.querySelector('[type="submit"]');
  const status=document.getElementById('form-status');
  const resting=submit.textContent;
  form.addEventListener('submit',event=>{
    if(submitting){event.preventDefault();return;}
    submitting=true;
    submit.disabled=true;submit.setAttribute('aria-busy','true');
    submit.textContent=copy.sending;status.textContent=copy.sending;
  });
  window.addEventListener('pageshow',()=>{
    submitting=false;submit.disabled=false;submit.removeAttribute('aria-busy');
    submit.textContent=resting;status.textContent='';
  });
});
