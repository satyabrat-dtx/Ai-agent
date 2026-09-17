# DB2ADMIN.LOGFINIMPORTFC

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 90
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 203347

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(5) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `BUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 3 | `VENDORCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 4 | `VENDORCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 5 | `PURCHASEORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 6 | `PURCHASEORDERCODE` | CHAR(15) |  |  |  |  |
| 7 | `FCLETTERDATE` | DATE |  |  |  |  |
| 8 | `STATUS` | CHAR(3) |  |  |  |  |
| 9 | `BANKCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 10 | `BANKCODE` | CHAR(20) |  |  |  |  |
| 11 | `POCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 12 | `POVALUE` | DECIMAL(18,5) |  |  |  |  |
| 13 | `TOCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 14 | `FCRATE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 15 | `FCVALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 16 | `USDVALUE` | DECIMAL(18,5) |  |  |  |  |
| 17 | `UTILISEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 18 | `ADJUSTAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 19 | `VALUE` | DECIMAL(18,5) |  |  |  |  |
| 20 | `CANCELLEDVALUE` | DECIMAL(18,5) |  |  |  |  |
| 21 | `UNUTILISEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 22 | `DUEDATEFROM` | DATE |  |  |  |  |
| 23 | `DUEDATETO` | DATE |  |  |  |  |
| 24 | `ITEMDESCRIPTION` | CHAR(50) |  |  |  |  |
| 25 | `REMARKS` | VARCHAR(500) |  |  |  |  |
| 26 | `BANKREFNUMBER` | CHAR(50) |  |  |  |  |
| 27 | `ADVICEDDATE` | DATE |  |  |  |  |
| 28 | `BANKCHARGESGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 29 | `BANKCHARGESGLCODE` | CHAR(20) |  |  |  |  |
| 30 | `BANKCHARGES` | DECIMAL(18,5) |  |  |  |  |
| 31 | `STEP` | CHAR(1) |  |  |  |  |
| 32 | `BANKCHARGESACTUAL` | DECIMAL(18,5) |  |  |  |  |
| 33 | `PCFINBVSPPROFITCENTERCODE` | CHAR(10) |  |  |  |  |
| 34 | `PCCOSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 35 | `NARRATION` | CHAR(50) |  |  |  |  |
| 36 | `TENOR` | CHAR(3) |  |  |  |  |
| 37 | `POSTINGDATE` | DATE |  |  |  |  |
| 38 | `CGSTVALUE` | DECIMAL(18,5) |  |  |  |  |
| 39 | `SGSTVALUE` | DECIMAL(18,5) |  |  |  |  |
| 40 | `CGSTGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 41 | `CGSTGLCODE` | CHAR(20) |  |  |  |  |
| 42 | `SGSTGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 43 | `SGSTGLCODE` | CHAR(20) |  |  |  |  |
| 44 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 45 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 46 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 47 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 48 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 49 | `CANCELLATIONDATE` | DATE |  |  |  |  |
| 50 | `RECOMMDAUTHDATE` | DATE |  |  |  |  |
| 51 | `CANCELLATIONRATE` | DECIMAL(18,5) |  |  |  |  |
| 52 | `LOSSORGAINGLACCOUNTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 53 | `LOSSORGAINGLACCOUNTCODE` | CHAR(20) |  |  |  |  |
| 54 | `LOSSORGAINCHARGES` | DECIMAL(18,5) |  |  |  |  |
| 55 | `ROUNDOFDIFFERENCE` | DECIMAL(18,5) |  |  |  |  |
| 56 | `IMPORTINTERESTGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 57 | `IMPORTINTERESTGLCODE` | CHAR(20) |  |  |  |  |
| 58 | `IMPORTINTERESTCHARGES` | DECIMAL(18,5) |  |  |  |  |
| 59 | `CANCELBANKCHARGESGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 60 | `CANCELBANKCHARGESGLCODE` | CHAR(20) |  |  |  |  |
| 61 | `CANCELBANKCHARGESMANUAL` | DECIMAL(18,5) |  |  |  |  |
| 62 | `CANCELBANKCHARGESACTUAL` | DECIMAL(18,5) |  |  |  |  |
| 63 | `CANCELPOSTINGDATE` | DATE |  |  |  |  |
| 64 | `CANCELCGST` | DECIMAL(18,5) |  |  |  |  |
| 65 | `CANCELSGST` | DECIMAL(18,5) |  |  |  |  |
| 66 | `CANCELCGSTGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 67 | `CANCELCGSTGLCODE` | CHAR(20) |  |  |  |  |
| 68 | `CANCELSGSTGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 69 | `CANCELSGSTGLCODE` | CHAR(20) |  |  |  |  |
| 70 | `CANCELCCFINBVSPPCENTERCODE` | CHAR(10) |  |  |  |  |
| 71 | `CANCELCCCOSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 72 | `CANFINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 73 | `CANFINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 74 | `CANFINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 75 | `CANFINDOCSTATGRPCODE` | CHAR(6) |  |  |  |  |
| 76 | `CANFINDOCCODE` | CHAR(15) |  |  |  |  |
| 77 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 78 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 79 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 80 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 81 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 82 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 83 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 84 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 85 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 86 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 87 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 88 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 89 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINIMPORTFC.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.
- child `LOGFINIMPORTFCPAYMENT`.`FATHERID` → this table's `ABSUNIQUEID` (medium confidence)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.BUSINESSUNITCODE,
       t.VENDORCUSTOMERSUPPLIERTYPE,
       t.VENDORCUSTOMERSUPPLIERCODE,
       t.PURCHASEORDERCOUNTERCODE,
       t.PURCHASEORDERCODE,
       t.FCLETTERDATE,
       t.STATUS,
       t.BANKCOMPANYCODE,
       t.BANKCODE,
       t.POCURRENCYCODE
FROM   DB2ADMIN.LOGFINIMPORTFC t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
