# DB2ADMIN.LOGFINALLOCATIONDEFN

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 49
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 228660

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(8) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `MAINSEQUENCE` | DECIMAL(8,0) | NOT NULL |  |  |  |
| 6 | `SUBSEQUENCE` | DECIMAL(8,0) | NOT NULL |  |  |  |
| 7 | `BUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 8 | `PROFITCENTREPROFITCENTERCODE` | CHAR(10) |  |  |  |  |
| 9 | `COSTCENTRECOSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 10 | `GLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 11 | `GLCODE` | CHAR(20) |  |  |  |  |
| 12 | `FIRSTSEGUGENGRPTECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 13 | `FIRSTSEGUGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 14 | `FIRSTSEGCODE` | CHAR(10) |  |  |  |  |
| 15 | `SNDSEGUGENGRPTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 16 | `SNDSEGUGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 17 | `SECONDSEGCODE` | CHAR(10) |  |  |  |  |
| 18 | `THIRDSEGUGENGRPTECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 19 | `THIRDSEGUGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 20 | `THIRDSEGCODE` | CHAR(10) |  |  |  |  |
| 21 | `FRSEGUGENGROUPTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 22 | `FRSEGUSERGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 23 | `FOURTHSEGCODE` | CHAR(10) |  |  |  |  |
| 24 | `FIFTHSEGUGENGRPTECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 25 | `FIFTHSEGUGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 26 | `FIFTHSEGCODE` | CHAR(10) |  |  |  |  |
| 27 | `SIXTHSEGUGENGRPTECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 28 | `SIXTHSEGUGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 29 | `SIXTHSEGCODE` | CHAR(10) |  |  |  |  |
| 30 | `SESEGUGENGROUPTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 31 | `SESEGUSERGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 32 | `SEVENTHSEGCODE` | CHAR(10) |  |  |  |  |
| 33 | `FROMDATE` | DATE | NOT NULL |  |  | Inclusive start of a validity period. |
| 34 | `TODATE` | DATE |  |  |  | End of a validity period. |
| 35 | `VALIDFLAG` | SMALLINT | NOT NULL |  |  |  |
| 36 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 37 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 38 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 39 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 40 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 41 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 42 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 43 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 44 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 45 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 46 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 47 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 48 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINALLOCATIONDEFN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.
- child `LOGFINALLOCATIONDEFNDETAIL`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.MAINSEQUENCE,
       t.SUBSEQUENCE,
       t.BUSINESSUNITCODE,
       t.PROFITCENTREPROFITCENTERCODE,
       t.COSTCENTRECOSTCENTERCODE,
       t.GLCOMPANYCODE,
       t.GLCODE
FROM   DB2ADMIN.LOGFINALLOCATIONDEFN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
