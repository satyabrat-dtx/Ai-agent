# DB2ADMIN.LOGFINEXPREALISATION

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 104
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 203017

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(15) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `BUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 3 | `NEGOTIATIONCODE` | CHAR(10) |  |  |  |  |
| 4 | `BANKCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 5 | `BANKCODE` | CHAR(20) |  |  |  |  |
| 6 | `BANKOTHERCHARGESCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 7 | `BANKOTHERCHARGESCODE` | CHAR(20) |  |  |  |  |
| 8 | `CUSTOMERCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 9 | `CUSTOMERCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 10 | `DUEDATE` | DATE |  |  |  |  |
| 11 | `NEGOTIATEDVALUE` | DECIMAL(18,5) |  |  |  |  |
| 12 | `REALIZEDVALUE` | DECIMAL(18,5) |  |  |  |  |
| 13 | `REALIZEDVALUEFC` | DECIMAL(18,5) |  |  |  |  |
| 14 | `EXCHANGERATE` | DECIMAL(18,5) |  |  |  |  |
| 15 | `CURRENTREALIZEDVALUE` | DECIMAL(18,5) |  |  |  |  |
| 16 | `COSTCENTERFINBVSPPCENTERCODE` | CHAR(10) |  |  |  |  |
| 17 | `COSTCENTERCOSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 18 | `REALIZATIONDATE` | DATE |  |  |  |  |
| 19 | `ACCEPTANCEDATE` | DATE |  |  |  |  |
| 20 | `BANKREFERENCEDATE` | DATE |  |  |  |  |
| 21 | `BANKDATE` | DATE |  |  |  |  |
| 22 | `POSTINGDATE` | DATE |  |  |  |  |
| 23 | `INTERESTRATE` | DECIMAL(5,2) |  |  |  |  |
| 24 | `INTERESTREFUND` | DECIMAL(18,5) |  |  |  |  |
| 25 | `INTERESTGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 26 | `INTERESTGLCODE` | CHAR(20) |  |  |  |  |
| 27 | `OTHERBANKCHARGES` | DECIMAL(18,5) |  |  |  |  |
| 28 | `FCRATE` | DECIMAL(5,2) |  |  |  |  |
| 29 | `INRVALUE` | DECIMAL(18,5) |  |  |  |  |
| 30 | `OVERDUEINTEREST` | DECIMAL(18,5) |  |  |  |  |
| 31 | `OTHERCHARGES` | DECIMAL(18,5) |  |  |  |  |
| 32 | `NETTOBANK` | DECIMAL(18,5) |  |  |  |  |
| 33 | `REMARKS` | VARCHAR(370) |  |  |  |  |
| 34 | `CGSTVALUE` | DECIMAL(18,5) |  |  |  |  |
| 35 | `SGSTVALUE` | DECIMAL(18,5) |  |  |  |  |
| 36 | `CGSTGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 37 | `CGSTGLCODE` | CHAR(20) |  |  |  |  |
| 38 | `SGSTGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 39 | `SGSTGLCODE` | CHAR(20) |  |  |  |  |
| 40 | `SUBVENTIONINTERESTRATE` | DECIMAL(5,2) |  |  |  |  |
| 41 | `INTERESTSUBVENTIONREFUND` | DECIMAL(18,5) |  |  |  |  |
| 42 | `INTERESTSUBVENTIONOVERDUE` | DECIMAL(18,5) |  |  |  |  |
| 43 | `INTERESTSGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 44 | `INTERESTSUBVENTIONGLCODE` | CHAR(20) |  |  |  |  |
| 45 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 46 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 47 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 48 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 49 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 50 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 51 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 52 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 53 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 54 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 55 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 56 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 57 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 58 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 59 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 60 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 61 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 62 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 63 | `NEGOTIATEDVALUEFC` | DECIMAL(18,5) |  |  |  |  |
| 64 | `NONNEGOTIATEDVALUEFC` | DECIMAL(18,5) |  |  |  |  |
| 65 | `NONNEGOTIATEDEXCHANGERATE` | DECIMAL(18,5) |  |  |  |  |
| 66 | `NONNEGOTIATEDVALUECC` | DECIMAL(18,5) |  |  |  |  |
| 67 | `REMAININGCRNTRELIZEDVLUINCC` | DECIMAL(18,5) |  |  |  |  |
| 68 | `EXCHANGEDIFFERENCE` | DECIMAL(18,5) |  |  |  |  |
| 69 | `BOENO` | CHAR(10) |  |  |  |  |
| 70 | `MARKETVALUEUTILIZEDFC` | DECIMAL(18,5) |  |  |  |  |
| 71 | `MARKETRATE` | DECIMAL(18,5) |  |  |  |  |
| 72 | `MARKETVALUEUTILIZEDCC` | DECIMAL(18,5) |  |  |  |  |
| 73 | `FORWARDCONTRACTVALUEUTILIZEDFC` | DECIMAL(18,5) |  |  |  |  |
| 74 | `FORWARDCONTRACTWIGHTEDAVGRATE` | DECIMAL(18,5) |  |  |  |  |
| 75 | `FORWARDCONTRACTVALUEUTILIZEDCC` | DECIMAL(18,5) |  |  |  |  |
| 76 | `PACKINGCREDITVALUEUTILIZEDCC` | DECIMAL(18,5) |  |  |  |  |
| 77 | `PACKINGCREDITGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 78 | `PACKINGCREDITGLCODE` | CHAR(20) |  |  |  |  |
| 79 | `CLAIMVALUE2` | DECIMAL(18,5) |  |  |  |  |
| 80 | `CLAIMGL2COMPANYCODE` | CHAR(3) |  |  |  |  |
| 81 | `CLAIMGL2CODE` | CHAR(20) |  |  |  |  |
| 82 | `BANKCHARGESVALUE2` | DECIMAL(18,5) |  |  |  |  |
| 83 | `BANKCHARGESGL2COMPANYCODE` | CHAR(3) |  |  |  |  |
| 84 | `BANKCHARGESGL2CODE` | CHAR(20) |  |  |  |  |
| 85 | `AGENCYCOMMISIONVALUE2` | DECIMAL(18,5) |  |  |  |  |
| 86 | `AGENCYCOMMISIONGL2COMPANYCODE` | CHAR(3) |  |  |  |  |
| 87 | `AGENCYCOMMISIONGL2CODE` | CHAR(20) |  |  |  |  |
| 88 | `EXCHANGEDIFFERENCEGLCMYCODE` | CHAR(3) |  |  |  |  |
| 89 | `EXCHANGEDIFFERENCEGLCODE` | CHAR(20) |  |  |  |  |
| 90 | `CREDIT` | SMALLINT | NOT NULL |  |  |  |
| 91 | `DEBIT` | SMALLINT | NOT NULL |  |  |  |
| 92 | `CURRENTACAMT` | DECIMAL(18,5) |  |  |  |  |
| 93 | `CURRENTACGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 94 | `CURRENTACGLCODE` | CHAR(20) |  |  |  |  |
| 95 | `PCFCINFOREIGNCURRENCY` | DECIMAL(18,5) |  |  |  |  |
| 96 | `PCFCRATE` | DECIMAL(18,5) |  |  |  |  |
| 97 | `PCFCVALUEININR` | DECIMAL(18,5) |  |  |  |  |
| 98 | `CGSTVALUE2` | DECIMAL(18,5) |  |  |  |  |
| 99 | `SGSTVALUE2` | DECIMAL(18,5) |  |  |  |  |
| 100 | `CGSTGL2COMPANYCODE` | CHAR(3) |  |  |  |  |
| 101 | `CGSTGL2CODE` | CHAR(20) |  |  |  |  |
| 102 | `SGSTGL2COMPANYCODE` | CHAR(3) |  |  |  |  |
| 103 | `SGSTGL2CODE` | CHAR(20) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINEXPREALISATION.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.
- child `LOGFINEXPREALISATIONDETAIL`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.BUSINESSUNITCODE,
       t.NEGOTIATIONCODE,
       t.BANKCOMPANYCODE,
       t.BANKCODE,
       t.BANKOTHERCHARGESCOMPANYCODE,
       t.BANKOTHERCHARGESCODE,
       t.CUSTOMERCUSTOMERSUPPLIERTYPE,
       t.CUSTOMERCUSTOMERSUPPLIERCODE,
       t.DUEDATE,
       t.NEGOTIATEDVALUE
FROM   DB2ADMIN.LOGFINEXPREALISATION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
