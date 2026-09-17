# DB2ADMIN.LOGBASECUSTOMIZEDOPTIONS

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 76
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 212741

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `INTRASTATHANDLING` | SMALLINT | NOT NULL |  |  |  |
| 2 | `VOLUMEUNITCODE` | CHAR(3) |  |  |  |  |
| 3 | `CHECKALLOCATIONHEADERCODE` | CHAR(20) |  |  |  |  |
| 4 | `CHECKALLOCATIONCODE` | CHAR(20) |  |  |  |  |
| 5 | `ALLOCATIONIMPMGRCODE` | CHAR(20) |  |  |  |  |
| 6 | `ALLQTYMODIFYANDDETAIL` | SMALLINT | NOT NULL |  |  |  |
| 7 | `SENDEMAILCODE` | CHAR(20) |  |  |  |  |
| 8 | `MULTIMEDIAMANAGERCODE` | CHAR(20) |  |  |  |  |
| 9 | `FINANCIALACCOUNTINGTYPECODE` | CHAR(2) |  |  |  |  |
| 10 | `MANAGEMENTACCOUNTINGTYPECODE` | CHAR(2) |  |  |  |  |
| 11 | `CUSTOMERSUPPLIERLOGMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 12 | `PORTFOLIOTMPLOGMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 13 | `PROJECTLOGMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 14 | `DEFPROJECTBUDGETBYPLANNINGRUN` | INTEGER | NOT NULL |  |  |  |
| 15 | `CURRENCYPOLICYREFERENCECODE` | CHAR(20) |  |  |  |  |
| 16 | `DESCRIPTIONCHANGEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 17 | `QTYRECALCULATIONSKIPPLYREFCODE` | CHAR(20) |  |  |  |  |
| 18 | `DEFCHILDPRODUCTCREATIONPOLCODE` | CHAR(20) |  |  |  |  |
| 19 | `CHECKPROJECTCODE` | CHAR(20) |  |  |  |  |
| 20 | `STATISTICALGROUPLABEL` | VARCHAR(80) |  |  |  |  |
| 21 | `CONTAINERLABEL` | VARCHAR(80) |  |  |  |  |
| 22 | `CUSTOMERCOUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 23 | `CUSTOMERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 24 | `SUPPLIERCOUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 25 | `SUPPLIERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 26 | `INTERNALCOUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 27 | `INTERNALCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 28 | `ALLOCATIONCOUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 29 | `ALLOCATIONCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 30 | `DEFINITIVEELMNUMBERINGCMYCODE` | CHAR(3) |  |  |  |  |
| 31 | `DEFINITIVEELEMENTNUMBERINGCODE` | CHAR(8) |  |  |  |  |
| 32 | `QUALITYCOUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 33 | `QUALITYCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 34 | `FIRSTMEASUREMENTTYPEDES` | CHAR(30) |  |  |  |  |
| 35 | `SNDMEASUREMENTTYPEDESCRIPTION` | CHAR(30) |  |  |  |  |
| 36 | `THIRDMEASUREMENTTYPEDES` | CHAR(30) |  |  |  |  |
| 37 | `FOURTHMEASUREMENTTYPEDES` | CHAR(30) |  |  |  |  |
| 38 | `FIFTHMEASUREMENTTYPEDES` | CHAR(30) |  |  |  |  |
| 39 | `LGLWHSFIRSTUSERGRPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 40 | `LGLWHSFIRSTUSERGRPCODE` | CHAR(3) |  |  |  |  |
| 41 | `LGLWHSSECONDUSERGRPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 42 | `LGLWHSSECONDUSERGRPCODE` | CHAR(3) |  |  |  |  |
| 43 | `LGLWHSTHIRDUSERGRPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 44 | `LGLWHSTHIRDUSERGRPCODE` | CHAR(3) |  |  |  |  |
| 45 | `LGLWHSFOURTHUSERGRPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 46 | `LGLWHSFOURTHUSERGRPCODE` | CHAR(3) |  |  |  |  |
| 47 | `LGLWHSFIFTHUSERGRPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 48 | `LGLWHSFIFTHUSERGRPCODE` | CHAR(3) |  |  |  |  |
| 49 | `LOTFIRSTUSERGRPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 50 | `LOTFIRSTUSERGRPCODE` | CHAR(3) |  |  |  |  |
| 51 | `LOTSECONDUSERGRPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 52 | `LOTSECONDUSERGRPCODE` | CHAR(3) |  |  |  |  |
| 53 | `LOTTHIRDUSERGRPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 54 | `LOTTHIRDUSERGRPCODE` | CHAR(3) |  |  |  |  |
| 55 | `LOTFOURTHUSERGRPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 56 | `LOTFOURTHUSERGRPCODE` | CHAR(3) |  |  |  |  |
| 57 | `LOTFIFTHUSERGRPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 58 | `LOTFIFTHUSERGRPCODE` | CHAR(3) |  |  |  |  |
| 59 | `ELEMENTFIRSTUSERGRPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 60 | `ELEMENTFIRSTUSERGRPCODE` | CHAR(3) |  |  |  |  |
| 61 | `ELMSECONDUSERGRPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 62 | `ELEMENTSECONDUSERGRPCODE` | CHAR(3) |  |  |  |  |
| 63 | `ELEMENTTHIRDUSERGRPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 64 | `ELEMENTTHIRDUSERGRPCODE` | CHAR(3) |  |  |  |  |
| 65 | `ELMFOURTHUSERGRPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 66 | `ELEMENTFOURTHUSERGRPCODE` | CHAR(3) |  |  |  |  |
| 67 | `ELEMENTFIFTHUSERGRPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 68 | `ELEMENTFIFTHUSERGRPCODE` | CHAR(3) |  |  |  |  |
| 69 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 70 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 71 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 72 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 73 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 74 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 75 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGBASECUSTOMIZEDOPTIONS.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.INTRASTATHANDLING,
       t.VOLUMEUNITCODE,
       t.CHECKALLOCATIONHEADERCODE,
       t.CHECKALLOCATIONCODE,
       t.ALLOCATIONIMPMGRCODE,
       t.ALLQTYMODIFYANDDETAIL,
       t.SENDEMAILCODE,
       t.MULTIMEDIAMANAGERCODE,
       t.FINANCIALACCOUNTINGTYPECODE,
       t.MANAGEMENTACCOUNTINGTYPECODE,
       t.CUSTOMERSUPPLIERLOGMANAGEMENT
FROM   DB2ADMIN.LOGBASECUSTOMIZEDOPTIONS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
