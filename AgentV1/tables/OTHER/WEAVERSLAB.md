# DB2ADMIN.WEAVERSLAB

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 20
- **Primary key**: `COMPANYCODE`, `WEAVERSLABICSTABLECODE`, `WEAVERSLABCODE`, `EFFECTIVEFROMDATE`, `SERIALNO`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 162380

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `WEAVERSLABICSTABLECODE` | CHAR(4) | NOT NULL | PK | primary_key |  |
| 2 | `WEAVERSLABCODE` | CHAR(6) | NOT NULL | PK | primary_key |  |
| 3 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 4 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 5 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 6 | `EFFECTIVEFROMDATE` | DATE | NOT NULL | PK | primary_key |  |
| 7 | `EFFECTIVETODATE` | DATE |  |  |  |  |
| 8 | `SERIALNO` | INTEGER | NOT NULL | PK | primary_key |  |
| 9 | `RANGE1` | DECIMAL(5,2) |  |  |  |  |
| 10 | `RANGE2` | DECIMAL(5,2) |  |  |  |  |
| 11 | `RATE` | DECIMAL(8,2) |  |  |  |  |
| 12 | `CURRENCYCODE` | CHAR(4) |  | FK | foreign_key |  |
| 13 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 14 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 15 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 16 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 17 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 18 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 19 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `WEAVERSLAB.COMPANYCODE = COMPANY.CODE` |
| `CURRENCY_CURRENCY` | `CURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `WEAVERSLAB.CURRENCYCODE = CURRENCY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WEAVERSLABUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.WEAVERSLABICSTABLECODE,
       t.WEAVERSLABCODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.EFFECTIVEFROMDATE,
       t.EFFECTIVETODATE,
       t.SERIALNO,
       t.RANGE1,
       t.RANGE2,
       t.RATE
FROM   DB2ADMIN.WEAVERSLAB t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
