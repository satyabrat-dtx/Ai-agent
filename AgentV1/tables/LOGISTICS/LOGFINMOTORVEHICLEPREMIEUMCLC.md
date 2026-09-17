# DB2ADMIN.LOGFINMOTORVEHICLEPREMIEUMCLC

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 81
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 228794

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `BUSINESSUNITGROUPCODE` | CHAR(10) |  |  |  |  |
| 2 | `AGEOFVEHICLE` | DECIMAL(3,0) |  |  |  |  |
| 3 | `VEHICLETYPE` | INTEGER | NOT NULL |  |  |  |
| 4 | `VEHICLENUMBER` | CHAR(10) | NOT NULL |  |  |  |
| 5 | `DATEOFPREMIUMCALCULATION` | DATE | NOT NULL |  |  |  |
| 6 | `NOOFPASSENGERS` | DECIMAL(4,0) |  |  |  |  |
| 7 | `YEAROFMANUFACTURE` | DECIMAL(4,0) |  |  |  |  |
| 8 | `STDCUBICCAPACITYTW` | CHAR(2) |  |  |  |  |
| 9 | `STDCUBICCAPACITYPC` | CHAR(2) |  |  |  |  |
| 10 | `STDCUBICCAPACITYPV` | CHAR(2) |  |  |  |  |
| 11 | `NUMBEROFPASSENGERS1` | CHAR(2) |  |  |  |  |
| 12 | `SUMINSURED` | DECIMAL(18,5) |  |  |  |  |
| 13 | `DUEDATE` | DATE |  |  |  |  |
| 14 | `FINANCIALYEARCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 15 | `FINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 16 | `PREPAIDEXPENSE` | DECIMAL(18,5) |  |  |  |  |
| 17 | `CUBICCAPACITY` | INTEGER | NOT NULL |  |  |  |
| 18 | `RATEPERCENTAGE2` | DECIMAL(6,3) |  |  |  |  |
| 19 | `FIXEDAMOUNT2` | DECIMAL(18,5) |  |  |  |  |
| 20 | `PREMIUMPOLICY` | DECIMAL(18,5) |  |  |  |  |
| 21 | `PREMIUMVALUE` | DECIMAL(18,5) |  |  |  |  |
| 22 | `LESSIMTDISCOUNT` | DECIMAL(18,5) |  |  |  |  |
| 23 | `IMTDISCOUNTB` | DECIMAL(18,5) |  |  |  |  |
| 24 | `SUBTOTAL1` | DECIMAL(18,5) |  |  |  |  |
| 25 | `ADDZERODEP` | DECIMAL(6,3) |  |  |  |  |
| 26 | `VALUE2` | DECIMAL(18,5) |  |  |  |  |
| 27 | `SUBTOTAL2` | DECIMAL(18,5) |  |  |  |  |
| 28 | `LESSNILDEPRENEWALDISCOUNT` | DECIMAL(18,5) |  |  |  |  |
| 29 | `VALUE3` | DECIMAL(18,5) |  |  |  |  |
| 30 | `SUBTOTAL3` | DECIMAL(18,5) |  |  |  |  |
| 31 | `LESSNCB` | DECIMAL(18,5) |  |  |  |  |
| 32 | `VALUE4` | DECIMAL(18,5) |  |  |  |  |
| 33 | `TOTALOWNDAMAGE` | DECIMAL(18,5) |  |  |  |  |
| 34 | `MINIMUMODAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 35 | `THIRDPARTYLIABILITYPREMIUM` | DECIMAL(18,5) |  |  |  |  |
| 36 | `ADDPABENEFIT` | DECIMAL(18,5) |  |  |  |  |
| 37 | `NUMBEROFPASSENGERS3` | DECIMAL(18,5) |  |  |  |  |
| 38 | `NUMBEROFPASSENGERSAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 39 | `ADDLL` | DECIMAL(18,5) |  |  |  |  |
| 40 | `TOTAL` | DECIMAL(18,5) |  |  |  |  |
| 41 | `SUBTOTAL4` | DECIMAL(18,5) |  |  |  |  |
| 42 | `ADDGST` | DECIMAL(18,5) |  |  |  |  |
| 43 | `GSTAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 44 | `CGSTVALUE` | DECIMAL(18,5) |  |  |  |  |
| 45 | `SGSTVALUE` | DECIMAL(18,5) |  |  |  |  |
| 46 | `TOTALPREMIUMTOBEPAID` | DECIMAL(18,5) |  |  |  |  |
| 47 | `BUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 48 | `PROFITCENTERPROFITCENTERCODE` | CHAR(10) |  |  |  |  |
| 49 | `COSTCENTERCOSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 50 | `INSURENCEACCGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 51 | `INSURENCEACCGLCODE` | CHAR(20) |  |  |  |  |
| 52 | `ORDVENDORACCCSMSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 53 | `ORDVENDORACCCSMSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 54 | `CGSTGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 55 | `CGSTGLCODE` | CHAR(20) |  |  |  |  |
| 56 | `SGSTGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 57 | `SGSTGLCODE` | CHAR(20) |  |  |  |  |
| 58 | `POSTINGDATE` | DATE | NOT NULL |  |  |  |
| 59 | `POSTINGFLAG` | INTEGER | NOT NULL |  |  |  |
| 60 | `REMARKS` | VARCHAR(255) |  |  |  |  |
| 61 | `FLAG` | CHAR(15) |  |  |  |  |
| 62 | `SAPMESSAGE` | LONG VARCHAR |  |  |  |  |
| 63 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 64 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 65 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 66 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 67 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 68 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 69 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 70 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 71 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 72 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 73 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 74 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 75 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 76 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 77 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 78 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 79 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 80 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINMOTORVEHICLEPREMIEUMCLC.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.BUSINESSUNITGROUPCODE,
       t.AGEOFVEHICLE,
       t.VEHICLETYPE,
       t.VEHICLENUMBER,
       t.DATEOFPREMIUMCALCULATION,
       t.NOOFPASSENGERS,
       t.YEAROFMANUFACTURE,
       t.STDCUBICCAPACITYTW,
       t.STDCUBICCAPACITYPC,
       t.STDCUBICCAPACITYPV,
       t.NUMBEROFPASSENGERS1
FROM   DB2ADMIN.LOGFINMOTORVEHICLEPREMIEUMCLC t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
