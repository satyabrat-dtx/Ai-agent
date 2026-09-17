# DB2ADMIN.LOGFINITCSEGMAP

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 43
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 228730

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `NUMBERID` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 2 | `BUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 3 | `DOCUMENTTEMPLATECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 4 | `DOCUMENTTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 5 | `FROMDATE` | DATE | NOT NULL |  |  | Inclusive start of a validity period. |
| 6 | `TODATE` | DATE |  |  |  | End of a validity period. |
| 7 | `FIRSTUSERGROUPTYPE` | CHAR(3) |  |  |  |  |
| 8 | `FIRSTUGRPUGENGRPTECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 9 | `FIRSTUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 10 | `SECONDUSERGROUPTYPE` | CHAR(3) |  |  |  |  |
| 11 | `SNDUGRPUGENGRPTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 12 | `SECONDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 13 | `THIRDUSERGROUPTYPE` | CHAR(3) |  |  |  |  |
| 14 | `THIRDUGRPUGENGRPTECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 15 | `THIRDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 16 | `FOURTHUSERGROUPTYPE` | CHAR(3) |  |  |  |  |
| 17 | `FRUGRPUGENGRPTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 18 | `FOURTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 19 | `FIFTHUSERGROUPTYPE` | CHAR(3) |  |  |  |  |
| 20 | `FIFTHUGRPUGENGRPTECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 21 | `FIFTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 22 | `SIXTHUSERGROUPTYPE` | CHAR(3) |  |  |  |  |
| 23 | `SIXTHUGRPUGENGRPTECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 24 | `SIXTHUSERGROUPCODE` | CHAR(10) |  |  |  |  |
| 25 | `SEVENTHUSERGROUPTYPE` | CHAR(3) |  |  |  |  |
| 26 | `SEUGRPUGENGRPTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 27 | `SEVENTHUSERGROUPCODE` | CHAR(10) |  |  |  |  |
| 28 | `COSTCENTRECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 29 | `COSTCENTRECODE` | CHAR(20) |  |  |  |  |
| 30 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 31 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 32 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 33 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 34 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 35 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 36 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 37 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 38 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 39 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 40 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 41 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 42 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINITCSEGMAP.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.
- child `LOGFINITCSEGMAPDETAIL`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.NUMBERID,
       t.BUSINESSUNITCODE,
       t.DOCUMENTTEMPLATECOMPANYCODE,
       t.DOCUMENTTEMPLATECODE,
       t.FROMDATE,
       t.TODATE,
       t.FIRSTUSERGROUPTYPE,
       t.FIRSTUGRPUGENGRPTECOMPANYCODE,
       t.FIRSTUSERGRPCODE,
       t.SECONDUSERGROUPTYPE,
       t.SNDUGRPUGENGRPTYPECOMPANYCODE
FROM   DB2ADMIN.LOGFINITCSEGMAP t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
