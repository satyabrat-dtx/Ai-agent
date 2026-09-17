# DB2ADMIN.LOGFINEXPADVANCE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 71
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 202156

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(5) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `BUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 3 | `ADVANCETYPE` | CHAR(1) |  |  |  |  |
| 4 | `FINANCIALYEARCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 5 | `FINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 6 | `REFERENCENOCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 7 | `REFERENCENOCODE` | CHAR(15) |  |  |  |  |
| 8 | `BANKGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 9 | `BANKGLCODE` | CHAR(20) |  |  |  |  |
| 10 | `SUBLEDGERCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 11 | `SUBLEDGERCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 12 | `REMITTER` | CHAR(100) |  |  |  |  |
| 13 | `BANKREFNO` | CHAR(20) |  |  |  |  |
| 14 | `BANKREFDATE` | DATE |  |  |  |  |
| 15 | `VALUEDATE` | DATE |  |  |  |  |
| 16 | `BANKCHARGESCALCULATEDINR` | DECIMAL(18,5) |  |  |  |  |
| 17 | `BANKCHARGESINR` | DECIMAL(18,5) |  |  |  |  |
| 18 | `BANKCHARGESGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 19 | `BANKCHARGESGLCODE` | CHAR(20) |  |  |  |  |
| 20 | `OTHERCHARGESCALCULATED` | DECIMAL(18,5) |  |  |  |  |
| 21 | `OTHERCHARGES` | DECIMAL(18,5) |  |  |  |  |
| 22 | `OTHERCHARGESGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 23 | `OTHERCHARGESGLCODE` | CHAR(20) |  |  |  |  |
| 24 | `OTHERCHARGESFC` | DECIMAL(18,5) |  |  |  |  |
| 25 | `EXCHANGERATE` | DECIMAL(18,5) |  |  |  |  |
| 26 | `OTHERCHARGESFCGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 27 | `OTHERCHARGESFCGLCODE` | CHAR(20) |  |  |  |  |
| 28 | `CURRENCYSCODE` | CHAR(4) |  |  |  |  |
| 29 | `ADVANCEAMOUNTUSD` | DECIMAL(18,5) |  |  |  |  |
| 30 | `DOCUMENTCURRENCY` | CHAR(4) |  |  |  |  |
| 31 | `COSTFINBVSPPROFITCENTERCODE` | CHAR(10) |  |  |  |  |
| 32 | `COSTCOSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 33 | `ADVANCEAMOUNTINR` | DECIMAL(18,5) |  |  |  |  |
| 34 | `POSTINGDATE` | DATE |  |  |  |  |
| 35 | `SPOTRATE` | DECIMAL(18,5) |  |  |  |  |
| 36 | `USDVALUE` | DECIMAL(18,5) |  |  |  |  |
| 37 | `STATUS` | CHAR(1) |  |  |  |  |
| 38 | `UTILIZEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 39 | `CGSTVALUE` | DECIMAL(18,5) |  |  |  |  |
| 40 | `SGSTVALUE` | DECIMAL(18,5) |  |  |  |  |
| 41 | `CGSTGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 42 | `CGSTGLCODE` | CHAR(20) |  |  |  |  |
| 43 | `SGSTGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 44 | `SGSTGLCODE` | CHAR(20) |  |  |  |  |
| 45 | `FCVALUE` | DECIMAL(18,5) |  |  |  |  |
| 46 | `FCCURRENCY` | DECIMAL(18,5) |  |  |  |  |
| 47 | `UTILIZEDVALUE` | DECIMAL(18,5) |  |  |  |  |
| 48 | `BUYERAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 49 | `REMARKS` | VARCHAR(200) |  |  |  |  |
| 50 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 51 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 52 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 53 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 54 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 55 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 56 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 57 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 58 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 59 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 60 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 61 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 62 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 63 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 64 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 65 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 66 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 67 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 68 | `PCFCINFOREIGNCURRENCY` | DECIMAL(18,5) |  |  |  |  |
| 69 | `PCFCRATE` | DECIMAL(18,5) |  |  |  |  |
| 70 | `PCFCVALUEININR` | DECIMAL(18,5) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINEXPADVANCE.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.BUSINESSUNITCODE,
       t.ADVANCETYPE,
       t.FINANCIALYEARCOMPANYCODE,
       t.FINANCIALYEARCODE,
       t.REFERENCENOCOUNTERCODE,
       t.REFERENCENOCODE,
       t.BANKGLCOMPANYCODE,
       t.BANKGLCODE,
       t.SUBLEDGERCUSTOMERSUPPLIERTYPE,
       t.SUBLEDGERCUSTOMERSUPPLIERCODE
FROM   DB2ADMIN.LOGFINEXPADVANCE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
