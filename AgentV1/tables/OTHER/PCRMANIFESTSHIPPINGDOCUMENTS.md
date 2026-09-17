# DB2ADMIN.PCRMANIFESTSHIPPINGDOCUMENTS

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `PCRMANIFESTCOMPANYCODE`, `PCRMANIFESTMANIFESTCODE`, `PROVISIONALCOUNTERCODE`, `PROVISIONALCODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 111816

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PCRMANIFESTCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `PCRMANIFESTMANIFESTCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `PROVISIONALCOUNTERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 3 | `PROVISIONALCOUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 4 | `PROVISIONALCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 5 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `PCRMANIFEST_MANIFESTSHIPPINGDOCUMENTS` | `PCRMANIFESTCOMPANYCODE`, `PCRMANIFESTMANIFESTCODE` | [`PCRMANIFEST`](../OTHER/PCRMANIFEST.md) | `COMPANYCODE`, `MANIFESTCODE` | RESTRICT | `PCRMANIFESTSHIPPINGDOCUMENTS.PCRMANIFESTCOMPANYCODE = PCRMANIFEST.COMPANYCODE AND PCRMANIFESTSHIPPINGDOCUMENTS.PCRMANIFESTMANIFESTCODE = PCRMANIFEST.MANIFESTCODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PCRMANIFESTSHPDOCUMENTSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.PCRMANIFESTCOMPANYCODE,
       t.PCRMANIFESTMANIFESTCODE,
       t.PROVISIONALCOUNTERCOMPANYCODE,
       t.PROVISIONALCOUNTERCODE,
       t.PROVISIONALCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.PCRMANIFESTSHIPPINGDOCUMENTS t
FETCH FIRST 100 ROWS ONLY;
```
