# DB2ADMIN.LOGPRICELIST

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 36
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 116369

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 2 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 3 | `ORDERTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 4 | `CODE` | CHAR(8) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 5 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 6 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 7 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 8 | `PRICELISTTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 9 | `REFERENCEDPRICELISTCODE` | CHAR(8) |  |  |  |  |
| 10 | `VALUEFORDYNAMICPRICELIST` | DECIMAL(18,5) |  |  |  |  |
| 11 | `PERCENTAGEFORDYNAMICPRICELIST` | DECIMAL(5,2) |  |  |  |  |
| 12 | `ROUNDINGMULTIPLYFACTOR` | DECIMAL(11,5) |  |  |  |  |
| 13 | `ROUNDINGCRITERIATYPE` | CHAR(2) |  |  |  |  |
| 14 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 15 | `EXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 16 | `MAXPOSITIVEPRCFOREXCHANGERATE` | DECIMAL(5,2) |  |  |  |  |
| 17 | `MAXNEGATIVEPRCFOREXCHANGERATE` | DECIMAL(5,2) |  |  |  |  |
| 18 | `ALLOWDIFFERENCES` | SMALLINT | NOT NULL |  |  |  |
| 19 | `MAXPOSITIVEPRCFORDOCPRICE` | DECIMAL(5,2) |  |  |  |  |
| 20 | `MAXNEGATIVEPRCFORDOCPRICE` | DECIMAL(5,2) |  |  |  |  |
| 21 | `ALLOWCONVERSION` | SMALLINT | NOT NULL |  |  |  |
| 22 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 23 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 24 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 25 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 26 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 27 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 28 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 29 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 30 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 31 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 32 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 33 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 34 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 35 | `PERCENTAGEDYNAMICASDIVISOR` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGPRICELIST.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.ORDERTYPE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.PRICELISTTYPE,
       t.REFERENCEDPRICELISTCODE,
       t.VALUEFORDYNAMICPRICELIST,
       t.PERCENTAGEFORDYNAMICPRICELIST
FROM   DB2ADMIN.LOGPRICELIST t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
