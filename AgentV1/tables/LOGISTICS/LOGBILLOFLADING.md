# DB2ADMIN.LOGBILLOFLADING

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 34
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 219020

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL |  |  | Division within a company; second-level organisational discriminator. |
| 2 | `CODE` | CHAR(20) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `BILLOFLADINGDATE` | DATE | NOT NULL |  |  |  |
| 4 | `SOURCE` | INTEGER | NOT NULL |  |  |  |
| 5 | `GROSSWEIGHT` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 6 | `NETWEIGHT` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 7 | `WEIGHINGUOMCODE` | CHAR(3) |  |  |  |  |
| 8 | `TOTALCONTAINERS` | INTEGER | NOT NULL |  |  |  |
| 9 | `TYPEOFSERVICE` | CHAR(25) |  |  |  |  |
| 10 | `TAXTEMPLATETEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 11 | `TAXTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 12 | `PLACECODE` | CHAR(3) |  |  |  |  |
| 13 | `PRINTDATE` | DATE |  |  |  |  |
| 14 | `ORIGINALBILLOFLADINGNO` | CHAR(25) |  |  |  |  |
| 15 | `ORIGINALBILLOFLADINGDATE` | DATE |  |  |  |  |
| 16 | `SHIPPINGAIRLINENAME` | CHAR(50) |  |  |  |  |
| 17 | `VESSELNO` | CHAR(50) |  |  |  |  |
| 18 | `ETA` | DATE |  |  |  |  |
| 19 | `ETD` | DATE |  |  |  |  |
| 20 | `CONTAINERNO` | CHAR(50) |  |  |  |  |
| 21 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 22 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 23 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 24 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 25 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 26 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 27 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 28 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 29 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 30 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 31 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 32 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 33 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGBILLOFLADING.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.CODE,
       t.BILLOFLADINGDATE,
       t.SOURCE,
       t.GROSSWEIGHT,
       t.NETWEIGHT,
       t.WEIGHINGUOMCODE,
       t.TOTALCONTAINERS,
       t.TYPEOFSERVICE,
       t.TAXTEMPLATETEMPLATETYPE,
       t.TAXTEMPLATECODE
FROM   DB2ADMIN.LOGBILLOFLADING t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
