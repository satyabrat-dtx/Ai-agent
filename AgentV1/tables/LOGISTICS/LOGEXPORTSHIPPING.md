# DB2ADMIN.LOGEXPORTSHIPPING

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 117
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 218668

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FSABSUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 1 | `EDIABSUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 2 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `DIVISIONCODE` | CHAR(3) | NOT NULL |  |  | Division within a company; second-level organisational discriminator. |
| 4 | `CODE` | CHAR(12) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 5 | `SHIPPINGBILLDATE` | DATE | NOT NULL |  |  |  |
| 6 | `LEONUMBER` | CHAR(35) |  |  |  |  |
| 7 | `LEODATE` | DATE |  |  |  |  |
| 8 | `BLDATE` | DATE |  |  |  |  |
| 9 | `CONSIGNEECUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 10 | `CONSIGNEECUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 11 | `SCHEMETYPECODE` | CHAR(3) |  |  |  |  |
| 12 | `CHACUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 13 | `CHACUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 14 | `BASICVALUEINR` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 15 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 16 | `BASICVALUEFC` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 17 | `EXCHANGERATE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 18 | `SHIPPINGBILLVALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 19 | `FREIGHTAMTFC` | DECIMAL(18,5) |  |  |  |  |
| 20 | `INSURANCEAMTFC` | DECIMAL(18,5) |  |  |  |  |
| 21 | `DISCOUNTAMTFC` | DECIMAL(18,5) |  |  |  |  |
| 22 | `PACKINGAMTFC` | DECIMAL(18,5) |  |  |  |  |
| 23 | `OTHERDEDUCTIONAMTFC` | DECIMAL(18,5) |  |  |  |  |
| 24 | `COMMISSIONAMTFC` | DECIMAL(18,5) |  |  |  |  |
| 25 | `FREIGHTAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 26 | `INSURANCEAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 27 | `DISCOUNTAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 28 | `PACKINGAMT` | DECIMAL(18,5) |  |  |  |  |
| 29 | `OTHERDEDUCTIONAMT` | DECIMAL(18,5) |  |  |  |  |
| 30 | `COMMISIONAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 31 | `FOBVALUEINR` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 32 | `FOBAFTERCOMMDED` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 33 | `FOBVALUEFC` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 34 | `DEPB` | DECIMAL(18,5) |  |  |  |  |
| 35 | `DBKWITHCENVAT` | DECIMAL(18,5) |  |  |  |  |
| 36 | `DBKWITHOUTCENVAT` | DECIMAL(18,5) |  |  |  |  |
| 37 | `CAPVALUE` | DECIMAL(18,5) |  |  |  |  |
| 38 | `RATEOFBENEIFITINR` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 39 | `RATEOFBENEIFITINRPOSTED` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 40 | `RBIAPPROVALNO` | CHAR(35) |  |  |  |  |
| 41 | `RBIAPPROVALDATE` | DATE |  |  |  |  |
| 42 | `PORTOFLOADINGCODE` | CHAR(10) |  |  |  |  |
| 43 | `RECEIVEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 44 | `RECEIVEDDATE` | DATE |  |  |  |  |
| 45 | `GROSSWEIGHT` | DECIMAL(15,5) |  |  |  |  |
| 46 | `NETWEIGHT` | DECIMAL(15,5) |  |  |  |  |
| 47 | `WEIGHTUMCODE` | CHAR(3) |  |  |  |  |
| 48 | `CUSTOMINVIOCECURRENCYCODE` | CHAR(4) |  |  |  |  |
| 49 | `FOBVALUEINIC` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 50 | `FOBVALUEINCC` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 51 | `TAXTEMPLATETEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 52 | `TAXTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 53 | `SYSTEMBENEFITAMOUNT` | DECIMAL(15,5) |  |  |  |  |
| 54 | `FULLEXPORTVALUE` | DECIMAL(18,5) |  |  |  |  |
| 55 | `USEDGRFORM` | INTEGER | NOT NULL |  |  |  |
| 56 | `FOOTERLINES` | VARCHAR(250) |  |  |  |  |
| 57 | `REMARKS` | VARCHAR(255) |  |  |  |  |
| 58 | `DESTINATIONCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 59 | `DEPBAPPLICATIONCODE` | CHAR(12) |  |  |  |  |
| 60 | `DBKAPPLICATIONCODE` | CHAR(12) |  |  |  |  |
| 61 | `FMSBENEFITCALCULATEDVALUE` | DECIMAL(18,5) |  |  |  |  |
| 62 | `FPSBENEFITCALCULATEDVALUE` | DECIMAL(18,5) |  |  |  |  |
| 63 | `MLFPSBENEFITCALCULATEDVALUE` | DECIMAL(18,5) |  |  |  |  |
| 64 | `FMSBENEFITPOSTINGVALUE` | DECIMAL(18,5) |  |  |  |  |
| 65 | `FPSBENEFITPOSTINGVALUE` | DECIMAL(18,5) |  |  |  |  |
| 66 | `MLFPSBENEFITPOSTINGVALUE` | DECIMAL(18,5) |  |  |  |  |
| 67 | `EDICALCULATEDVALUE` | DECIMAL(18,5) |  |  |  |  |
| 68 | `EDIPOSTEDVALUE` | DECIMAL(18,5) |  |  |  |  |
| 69 | `ESBBENEFITFLAG` | CHAR(15) |  |  |  |  |
| 70 | `ESBBENEFITMESSAGE` | LONG VARCHAR |  |  |  |  |
| 71 | `FOCUSFLAG` | CHAR(15) |  |  |  |  |
| 72 | `FOCUSMESSAGE` | LONG VARCHAR |  |  |  |  |
| 73 | `EDIFLAG` | CHAR(15) |  |  |  |  |
| 74 | `EDIMESSAGE` | LONG VARCHAR |  |  |  |  |
| 75 | `EPCOPYDATE` | DATE |  |  |  |  |
| 76 | `EPCOPYREMARKS` | VARCHAR(200) |  |  |  |  |
| 77 | `LANDINGDATE` | DATE |  |  |  |  |
| 78 | `LANDINGREMARKS` | VARCHAR(200) |  |  |  |  |
| 79 | `DATEOFUPLOADING` | DATE |  |  |  |  |
| 80 | `EBRCDATE` | DATE |  |  |  |  |
| 81 | `REALISEDVALUEFCC` | DECIMAL(18,5) |  |  |  |  |
| 82 | `EBRCREMARKS1` | VARCHAR(200) |  |  |  |  |
| 83 | `EBRCREMARKS2` | VARCHAR(200) |  |  |  |  |
| 84 | `EBRCREMARKS3` | VARCHAR(200) |  |  |  |  |
| 85 | `ACTUALVALUEFREIGHT` | DECIMAL(18,5) |  |  |  |  |
| 86 | `OCEANDATEOFUPLOADING` | DATE |  |  |  |  |
| 87 | `OCEANREMARKS1` | VARCHAR(200) |  |  |  |  |
| 88 | `OCEANREMARKS2` | VARCHAR(200) |  |  |  |  |
| 89 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 90 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 91 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 92 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 93 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 94 | `FINDOCBUSINESSUNITCODEFOCUS` | CHAR(10) |  |  |  |  |
| 95 | `FINDOCFINANCIALYEARCODEFOCUS` | DECIMAL(4,0) |  |  |  |  |
| 96 | `FINDOCTEMPLATECODEFOCUS` | CHAR(3) |  |  |  |  |
| 97 | `FINDOCSTCGROUPCODEFOCUS` | CHAR(6) |  |  |  |  |
| 98 | `FINDOCCODEFOCUS` | CHAR(15) |  |  |  |  |
| 99 | `FINDOCBUSINESSUNITCODEEDI` | CHAR(10) |  |  |  |  |
| 100 | `FINDOCFINANCIALYEARCODEEDI` | DECIMAL(4,0) |  |  |  |  |
| 101 | `FINDOCTEMPLATECODEEDI` | CHAR(3) |  |  |  |  |
| 102 | `FINDOCSTATISTICALGROUPCODEEDI` | CHAR(6) |  |  |  |  |
| 103 | `FINDOCCODEEDI` | CHAR(15) |  |  |  |  |
| 104 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 105 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 106 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 107 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 108 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 109 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 110 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 111 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 112 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 113 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 114 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 115 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 116 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGEXPORTSHIPPING.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.FSABSUNIQUEID,
       t.EDIABSUNIQUEID,
       t.COMPANYCODE,
       t.DIVISIONCODE,
       t.CODE,
       t.SHIPPINGBILLDATE,
       t.LEONUMBER,
       t.LEODATE,
       t.BLDATE,
       t.CONSIGNEECUSTOMERSUPPLIERTYPE,
       t.CONSIGNEECUSTOMERSUPPLIERCODE,
       t.SCHEMETYPECODE
FROM   DB2ADMIN.LOGEXPORTSHIPPING t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
