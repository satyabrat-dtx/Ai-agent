# DB2ADMIN.SCDC_BIN_SHOW_PROP

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDC_')
- **Roles**: `business_data`
- **Columns**: 62
- **Primary key**: `BP_IDENTIFIER`, `BP_WKST_CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 188562

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `BP_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `BP_WKST_CODE` | VARCHAR(10) | NOT NULL | PK | primary_key |  |
| 2 | `BP_PROPCODE1` | VARCHAR(5) |  |  |  |  |
| 3 | `BP_PROPCODE2` | VARCHAR(5) |  |  |  |  |
| 4 | `BP_PROPCODE3` | VARCHAR(5) |  |  |  |  |
| 5 | `BP_PROPCODE4` | VARCHAR(5) |  |  |  |  |
| 6 | `BP_PROPCODE5` | VARCHAR(5) |  |  |  |  |
| 7 | `BP_PROPCODE6` | VARCHAR(5) |  |  |  |  |
| 8 | `BP_PROPCODE7` | VARCHAR(5) |  |  |  |  |
| 9 | `BP_PROPCODE8` | VARCHAR(5) |  |  |  |  |
| 10 | `BP_PROPCODE9` | VARCHAR(5) |  |  |  |  |
| 11 | `BP_PROPCODE10` | VARCHAR(5) |  |  |  |  |
| 12 | `BP_PROPCODE11` | VARCHAR(5) |  |  |  |  |
| 13 | `BP_PROPCODE12` | VARCHAR(5) |  |  |  |  |
| 14 | `BP_PROPCODE13` | VARCHAR(5) |  |  |  |  |
| 15 | `BP_PROPCODE14` | VARCHAR(5) |  |  |  |  |
| 16 | `BP_PROPCODE15` | VARCHAR(5) |  |  |  |  |
| 17 | `BP_PROPCODE16` | VARCHAR(5) |  |  |  |  |
| 18 | `BP_PROPCODE17` | VARCHAR(5) |  |  |  |  |
| 19 | `BP_PROPCODE18` | VARCHAR(5) |  |  |  |  |
| 20 | `BP_PROPCODE19` | VARCHAR(5) |  |  |  |  |
| 21 | `BP_PROPCODE20` | VARCHAR(5) |  |  |  |  |
| 22 | `BP_PROPCODE21` | VARCHAR(5) |  |  |  |  |
| 23 | `BP_PROPCODE22` | VARCHAR(5) |  |  |  |  |
| 24 | `BP_PROPCODE23` | VARCHAR(5) |  |  |  |  |
| 25 | `BP_PROPCODE24` | VARCHAR(5) |  |  |  |  |
| 26 | `BP_PROPCODE25` | VARCHAR(5) |  |  |  |  |
| 27 | `BP_PROPCODE26` | VARCHAR(5) |  |  |  |  |
| 28 | `BP_PROPCODE27` | VARCHAR(5) |  |  |  |  |
| 29 | `BP_PROPCODE28` | VARCHAR(5) |  |  |  |  |
| 30 | `BP_PROPCODE29` | VARCHAR(5) |  |  |  |  |
| 31 | `BP_PROPCODE30` | VARCHAR(5) |  |  |  |  |
| 32 | `BP_PROPCODE31` | VARCHAR(5) |  |  |  |  |
| 33 | `BP_PROPCODE32` | VARCHAR(5) |  |  |  |  |
| 34 | `BP_PROPCODE33` | VARCHAR(5) |  |  |  |  |
| 35 | `BP_PROPCODE34` | VARCHAR(5) |  |  |  |  |
| 36 | `BP_PROPCODE35` | VARCHAR(5) |  |  |  |  |
| 37 | `BP_PROPCODE36` | VARCHAR(5) |  |  |  |  |
| 38 | `BP_PROPCODE37` | VARCHAR(5) |  |  |  |  |
| 39 | `BP_PROPCODE38` | VARCHAR(5) |  |  |  |  |
| 40 | `BP_PROPCODE39` | VARCHAR(5) |  |  |  |  |
| 41 | `BP_PROPCODE40` | VARCHAR(5) |  |  |  |  |
| 42 | `BP_PROPCODE41` | VARCHAR(5) |  |  |  |  |
| 43 | `BP_PROPCODE42` | VARCHAR(5) |  |  |  |  |
| 44 | `BP_PROPCODE43` | VARCHAR(5) |  |  |  |  |
| 45 | `BP_PROPCODE44` | VARCHAR(5) |  |  |  |  |
| 46 | `BP_PROPCODE45` | VARCHAR(5) |  |  |  |  |
| 47 | `BP_PROPCODE46` | VARCHAR(5) |  |  |  |  |
| 48 | `BP_PROPCODE47` | VARCHAR(5) |  |  |  |  |
| 49 | `BP_PROPCODE48` | VARCHAR(5) |  |  |  |  |
| 50 | `BP_PROPCODE49` | VARCHAR(5) |  |  |  |  |
| 51 | `BP_PROPCODE50` | VARCHAR(5) |  |  |  |  |
| 52 | `BP_PROPCODE51` | VARCHAR(5) |  |  |  |  |
| 53 | `BP_PROPCODE52` | VARCHAR(5) |  |  |  |  |
| 54 | `BP_PROPCODE53` | VARCHAR(5) |  |  |  |  |
| 55 | `BP_PROPCODE54` | VARCHAR(5) |  |  |  |  |
| 56 | `BP_PROPCODE55` | VARCHAR(5) |  |  |  |  |
| 57 | `BP_PROPCODE56` | VARCHAR(5) |  |  |  |  |
| 58 | `BP_PROPCODE57` | VARCHAR(5) |  |  |  |  |
| 59 | `BP_PROPCODE58` | VARCHAR(5) |  |  |  |  |
| 60 | `BP_PROPCODE59` | VARCHAR(5) |  |  |  |  |
| 61 | `BP_PROPCODE60` | VARCHAR(5) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.BP_IDENTIFIER,
       t.BP_WKST_CODE,
       t.BP_PROPCODE1,
       t.BP_PROPCODE2,
       t.BP_PROPCODE3,
       t.BP_PROPCODE4,
       t.BP_PROPCODE5,
       t.BP_PROPCODE6,
       t.BP_PROPCODE7,
       t.BP_PROPCODE8,
       t.BP_PROPCODE9,
       t.BP_PROPCODE10
FROM   DB2ADMIN.SCDC_BIN_SHOW_PROP t
FETCH FIRST 100 ROWS ONLY;
```
