function varargout = knot(varargin)

global  intersections
% KNOT MATLAB code for knot.fig
%      KNOT, by itself, creates a new KNOT or raises the existing
%      singleton*.
%
%      H = KNOT returns the handle to a new KNOT or the handle to
%      the existing singleton*.
%
%      KNOT('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in KNOT.M with the given input arguments.
%
%      KNOT('Property','Value',...) creates a new KNOT or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before knot_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to knot_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help knot

% Last Modified by GUIDE v2.5 21-Apr-2020 08:49:06

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @knot_OpeningFcn, ...
                   'gui_OutputFcn',  @knot_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before knot is made visible.
function knot_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to knot (see VARARGIN)

% Choose default command line output for knot
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes knot wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = knot_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;



function pdb_Callback(hObject, eventdata, handles)
% hObject    handle to pdb (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of pdb as text
%        str2double(get(hObject,'String')) returns contents of pdb as a double


% --- Executes during object creation, after setting all properties.
function pdb_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pdb (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','gray');
end






% --- Executes on button press in load.
function load_Callback(hObject, eventdata, handles)
% hObject    handle to load (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

filename = get(handles.pdb, 'string');
[coor,coor1] = knot_getcoor(sprintf('%s',filename),get(handles.connectfront,'Value'));
intersections = knot_draw(coor, 0, 1);
dlmwrite('currentcoor.txt',coor,'precision',16)



function angle_Callback(hObject, eventdata, handles)
% hObject    handle to angle (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of angle as text
%        str2double(get(hObject,'String')) returns contents of angle as a double


% --- Executes during object creation, after setting all properties.
function angle_CreateFcn(hObject, eventdata, handles)
% hObject    handle to angle (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','gray');
end


% --- Executes on button press in rotatex.
function rotatex_Callback(hObject, eventdata, handles)
% hObject    handle to rotatex (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

coor = load('currentcoor.txt');
var = get(handles.angle, 'string');
var = str2double(var);
coor = knot_rotx(coor, var);
intersections = knot_draw(coor, 0, 1);
dlmwrite('currentcoor.txt',coor,'precision',16)


% --- Executes on button press in center.
function center_Callback(hObject, eventdata, handles)
% hObject    handle to center (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

coor = load('currentcoor.txt');
coor = knot_center(coor);
intersections = knot_draw(coor, 0, 1);
dlmwrite('currentcoor.txt',coor,'precision',16)



function intersection_Callback(hObject, eventdata, handles)
% hObject    handle to intersection (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of intersection as text
%        str2double(get(hObject,'String')) returns contents of intersection as a double


% --- Executes during object creation, after setting all properties.
function intersection_CreateFcn(hObject, eventdata, handles)
% hObject    handle to intersection (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','gray');
end


% --- Executes on button press in loopmove.
function loopmove_Callback(hObject, eventdata, handles)
% hObject    handle to loopmove (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

coor = load('currentcoor.txt');
var = get(handles.intersection, 'string');
var = str2double(var);
intersections = knot_draw(coor, 0, 1);
coor = knot_loop_move(coor, intersections, var);
intersections = knot_draw(coor, 0, 1);
dlmwrite('currentcoor.txt',coor)



% --- Executes on button press in rotatey.
function rotatey_Callback(hObject, eventdata, handles)
% hObject    handle to rotatey (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

coor = load('currentcoor.txt');
var = get(handles.angle, 'string');
var = str2double(var);
coor = knot_roty(coor, var);
intersections = knot_draw(coor, 0, 1);
dlmwrite('currentcoor.txt',coor,'precision',16)


% --- Executes on button press in rotatez.
function rotatez_Callback(hObject, eventdata, handles)
% hObject    handle to rotatez (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

coor = load('currentcoor.txt');
var = get(handles.angle, 'string');
var = str2double(var);
coor = knot_rotz(coor, var);
intersections = knot_draw(coor, 0, 1);
dlmwrite('currentcoor.txt',coor,'precision',16)


% --- Executes on button press in connectfront.
function connectfront_Callback(hObject, eventdata, handles)
% hObject    handle to connectfront (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of connectfront
