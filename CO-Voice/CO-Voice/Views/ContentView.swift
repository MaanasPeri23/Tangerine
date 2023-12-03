//
//  ContentView.swift
//  CO-Voice
//
//  Created by Mohammad Yasir on 13/02/21.
//

import SwiftUI

struct ContentView: View {
    
    @ObservedObject var vm = VoiceViewModel()
    
    @State private var showingList = false
    @State private var showingAlert = false
    
    @State private var effect1 = false
    @State private var effect2 = false

    
    var body: some View {
        
        ZStack{
            
            Image("back")
                .resizable()
                .scaledToFill()
                .edgesIgnoringSafeArea(.all)
                
            
            VStack{
                HStack{
                    
                    Text("Tangerine")
                        .foregroundColor(.white)
                        .font(.system(size: 20 , weight : .bold))
                    
                    Spacer()
                    
                    Button(action: {
                        if vm.isRecording == true {
                            vm.stopRecording()
                        }
                        vm.fetchAllRecording()
                        showingList.toggle()
                    }) {
                        Image(systemName: "list.bullet")
                            .foregroundColor(.white)
                            .font(.system(size: 20, weight: .bold))
                    }.sheet(isPresented: $showingList, content: {
                        recordingListView()
                    })
                    
                }
                
                Spacer()
                
                if vm.isRecording {
                    
                    VStack(alignment : .leading , spacing : -5){
                        HStack (spacing : 3) {
                            Image(systemName: vm.isRecording && vm.toggleColor ? "circle.fill" : "circle")
                                .font(.system(size:10))
                                .foregroundColor(.red)
                            Text("Rec")
                        }
                        Text(vm.timer)
                            .font(.system(size:60))
                            .foregroundColor(.white)
                    }
                    
                } else {
                    VStack{
                        Text("Tap to record!!!")
                            .foregroundColor(.white)
                            .fontWeight(.bold)
                    }.frame(width: 300, height: 100, alignment: .center)
                    
                    
                }
                
                Spacer()
                Spacer()
                
                ZStack {
                    
                    
                    Image(systemName: vm.isRecording ? "stop.circle.fill" : "mic.circle.fill")
                        .foregroundColor(.white)
                        .font(.system(size: 45))
                        .onTapGesture {
                            if vm.isRecording == true {
                                vm.stopRecording()
                            } else {
                                vm.startRecording()
                                
                            }
                        }
                    
                    
                }
                
                Spacer()
                
            }
            .padding(.leading,25)
            .padding(.trailing,25)
            .padding(.top , 100)
            
            
        }
   
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
