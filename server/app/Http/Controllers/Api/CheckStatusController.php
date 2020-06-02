<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;

class CheckStatusController extends Controller
{
    public function check_status(Request $request)
    {
        return response()->json(['code' => 200, 'status' => 1]);
    }
}
