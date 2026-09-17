# DB2ADMIN.MARKET

- **Module**: `SALES` (low confidence — FK neighbourhood: 4 of 4 related tables are SALES)
- **Roles**: `business_data`
- **Columns**: 11
- **Primary key**: `CODE`
- **FK degree**: referenced by 6 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 27813

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CODE` | CHAR(10) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 1 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 2 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 3 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 4 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 5 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 6 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 7 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 8 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 9 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 10 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 6

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `MARKET_MARKET` | [`SALESDOCUMENT`](../SALES/SALESDOCUMENT.md) | `MARKETCODE` | `SALESDOCUMENT.MARKETCODE = MARKET.CODE` |
| `MARKET_MARKET` | [`SALESRELEASELINE`](../SALES/SALESRELEASELINE.md) | `MARKETCODE` | `SALESRELEASELINE.MARKETCODE = MARKET.CODE` |
| `MARKET_MARKET` | [`SALESORDER`](../SALES/SALESORDER.md) | `MARKETCODE` | `SALESORDER.MARKETCODE = MARKET.CODE` |
| `MARKET_MARKET` | [`ORDERPARTNER`](../CORE_MASTER/ORDERPARTNER.md) | `MARKETCODE` | `ORDERPARTNER.MARKETCODE = MARKET.CODE` |
| `MARKET_MARKET` | [`ORDERPARTNERSPECIALIZEDDATA`](../OTHER/ORDERPARTNERSPECIALIZEDDATA.md) | `MARKETCODE` | `ORDERPARTNERSPECIALIZEDDATA.MARKETCODE = MARKET.CODE` |
| `MARKET_MARKET` | [`SALESORDERTEMPLATE`](../SALES/SALESORDERTEMPLATE.md) | `MARKETCODE` | `SALESORDERTEMPLATE.MARKETCODE = MARKET.CODE` |

## Indexes

- `MARKETUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC
FROM   DB2ADMIN.MARKET t
FETCH FIRST 100 ROWS ONLY;
```
