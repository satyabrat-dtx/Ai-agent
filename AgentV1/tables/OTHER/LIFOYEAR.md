# DB2ADMIN.LIFOYEAR

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 11
- **Primary key**: `COMPANYCODE`, `YEAR`
- **FK degree**: referenced by 3 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 23119

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `YEAR` | DECIMAL(4,0) | NOT NULL | PK | primary_key |  |
| 2 | `INITIALDATE` | DATE |  |  |  |  |
| 3 | `FINALDATE` | DATE |  |  |  |  |
| 4 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 5 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 6 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 7 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 8 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 9 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 10 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 3

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `LIFOYEAR_FISCALYEAR` | [`LIFOHISTORY`](../OTHER/LIFOHISTORY.md) | `COMPANYCODE`, `FISCALYEARYEAR` | `LIFOHISTORY.COMPANYCODE = LIFOYEAR.COMPANYCODE AND LIFOHISTORY.FISCALYEARYEAR = LIFOYEAR.YEAR` |
| `LIFOYEAR_FISCALYEAR` | [`DEPBFINYEARTURNOVERDOMESTIC`](../OTHER/DEPBFINYEARTURNOVERDOMESTIC.md) | `DEPBDEFAULTCOMPANYCODE`, `FISCALYEARYEAR` | `DEPBFINYEARTURNOVERDOMESTIC.DEPBDEFAULTCOMPANYCODE = LIFOYEAR.COMPANYCODE AND DEPBFINYEARTURNOVERDOMESTIC.FISCALYEARYEAR = LIFOYEAR.YEAR` |
| `LIFOYEAR_FISCALYEAR` | [`DEPBFINYEARTURNOVEREXPORT`](../OTHER/DEPBFINYEARTURNOVEREXPORT.md) | `DEPBDEFAULTCOMPANYCODE`, `FISCALYEARYEAR` | `DEPBFINYEARTURNOVEREXPORT.DEPBDEFAULTCOMPANYCODE = LIFOYEAR.COMPANYCODE AND DEPBFINYEARTURNOVEREXPORT.FISCALYEARYEAR = LIFOYEAR.YEAR` |

## Indexes

- `LIFOYEARUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.YEAR,
       t.INITIALDATE,
       t.FINALDATE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC
FROM   DB2ADMIN.LIFOYEAR t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
