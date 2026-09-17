# DB2ADMIN.WRKRG1

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 32
- **Primary key**: `CREATIONTIMESTAMP`, `SEQNO`, `COMPANYCODE`, `DIVISIONCODE`, `RG1TEMPLATECODE`, `TARIFFCODE`, `ITDATE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 145554

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `SEQNO` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `GROUPING` | CHAR(20) |  |  |  |  |
| 4 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 5 | `RG1TEMPLATECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 6 | `TARIFFCODE` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 7 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 8 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 9 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 10 | `TYPE` | INTEGER | NOT NULL |  |  |  |
| 11 | `ITDATE` | DATE | NOT NULL | PK | primary_key |  |
| 12 | `ADDDEDUCT` | INTEGER | NOT NULL |  |  |  |
| 13 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 14 | `CUMQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 15 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 16 | `BALESCOUNT` | INTEGER | NOT NULL |  |  |  |
| 17 | `CUMBALESCOUNT` | INTEGER | NOT NULL |  |  |  |
| 18 | `CUMVALUE` | DECIMAL(18,5) |  |  |  |  |
| 19 | `WIDTH` | DECIMAL(18,5) |  |  |  |  |
| 20 | `CUMWIDTH` | DECIMAL(18,5) |  |  |  |  |
| 21 | `VALUE` | DECIMAL(18,5) |  |  |  |  |
| 22 | `PLANT` | CHAR(8) |  |  |  |  |
| 23 | `SQMTRS` | DECIMAL(18,5) |  |  |  |  |
| 24 | `CUMSQMTRS` | DECIMAL(18,5) |  |  |  |  |
| 25 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 26 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 27 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 28 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 29 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 30 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 31 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKRG1UID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.SEQNO,
       t.COMPANYCODE,
       t.GROUPING,
       t.DIVISIONCODE,
       t.RG1TEMPLATECODE,
       t.TARIFFCODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.TYPE,
       t.ITDATE
FROM   DB2ADMIN.WRKRG1 t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
