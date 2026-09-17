# DB2ADMIN.EINVOICEERROR

- **Module**: `EINVOICING` (high confidence — table name starts with 'EINVOIC')
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `COMPANYCODE`, `UNIQUEID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 236695

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `UNIQUEID` | BIGINT | NOT NULL | PK | primary_key |  |
| 2 | `EINVOICEHEADERUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 3 | `OWNERENTITYNAME` | CHAR(100) |  |  |  |  |
| 4 | `IMPORTREFERENCE` | VARCHAR(255) |  |  |  |  |
| 5 | `OWNERABSUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 6 | `SEQUENCEWITHINOWNER` | INTEGER | NOT NULL |  |  |  |
| 7 | `ERRORCONTEXT` | CHAR(2) | NOT NULL |  |  |  |
| 8 | `ERRORCODE` | CHAR(12) | NOT NULL |  |  |  |
| 9 | `RESUMED` | SMALLINT | NOT NULL |  |  |  |
| 10 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 11 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 12 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 13 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 14 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 15 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EINVOICEERRORUID` (ABSUNIQUEID)
- `EINVOICEERROR1` (COMPANYCODE, OWNERENTITYNAME, OWNERABSUNIQUEID)
- `EINVOICEERROR2` (COMPANYCODE, ERRORCONTEXT, IMPORTREFERENCE)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.UNIQUEID,
       t.EINVOICEHEADERUNIQUEID,
       t.OWNERENTITYNAME,
       t.IMPORTREFERENCE,
       t.OWNERABSUNIQUEID,
       t.SEQUENCEWITHINOWNER,
       t.ERRORCONTEXT,
       t.ERRORCODE,
       t.RESUMED,
       t.CREATIONDATETIME,
       t.CREATIONUSER
FROM   DB2ADMIN.EINVOICEERROR t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
