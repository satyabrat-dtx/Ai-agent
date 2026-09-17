# DB2ADMIN.ACTUALCOSTENTITYCLOSINGBLN

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 72
- **Primary key**: `ACTUALCOSTENTITYCOMPANYCODE`, `ACTUALCOSTENTITYNUMBERID`, `CLOSINGBALANCEFORDATE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 50992

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ACTUALCOSTENTITYCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `ACTUALCOSTENTITYNUMBERID` | DECIMAL(11,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `CLOSINGBALANCEFORDATE` | DATE | NOT NULL | PK | primary_key |  |
| 3 | `DYNAMICAVERAGECOSTTOTALVALUE` | DECIMAL(18,5) |  |  |  |  |
| 4 | `DYNAMICAVERAGECOSTTOTALQTY` | DECIMAL(15,5) |  |  |  |  |
| 5 | `DYNAMICAVERAGECOSTPERUNIT` | DECIMAL(18,5) |  |  |  |  |
| 6 | `PERCENTCATEGORY1` | DECIMAL(6,3) |  |  |  |  |
| 7 | `PERCENTCATEGORY2` | DECIMAL(6,3) |  |  |  |  |
| 8 | `PERCENTCATEGORY3` | DECIMAL(6,3) |  |  |  |  |
| 9 | `PERCENTCATEGORY4` | DECIMAL(6,3) |  |  |  |  |
| 10 | `PERCENTCATEGORY5` | DECIMAL(6,3) |  |  |  |  |
| 11 | `PERCENTCATEGORY6` | DECIMAL(6,3) |  |  |  |  |
| 12 | `CALCULATIONSTATUS` | CHAR(1) |  |  |  |  |
| 13 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 14 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 15 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 16 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 17 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 18 | `DYNAVGCOSTPERUNITBEFOREADDCST` | DECIMAL(18,5) |  |  |  |  |
| 19 | `DYNAVGCOSTTOTVALBEFOREADDCST` | DECIMAL(18,5) |  |  |  |  |
| 20 | `PERCENTCATEGORY7` | DECIMAL(6,3) |  |  |  |  |
| 21 | `PERCENTCATEGORY8` | DECIMAL(6,3) |  |  |  |  |
| 22 | `PERCENTCATEGORY9` | DECIMAL(6,3) |  |  |  |  |
| 23 | `PERCENTCATEGORY10` | DECIMAL(6,3) |  |  |  |  |
| 24 | `PERCENTCATEGORY11` | DECIMAL(6,3) |  |  |  |  |
| 25 | `PERCENTCATEGORY12` | DECIMAL(6,3) |  |  |  |  |
| 26 | `PERCENTCATEGORY0` | DECIMAL(6,3) |  |  |  |  |
| 27 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 28 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 29 | `DYNAMICAVERAGECOSTTOTVALSNDCUR` | DECIMAL(18,5) |  |  |  |  |
| 30 | `DYNAMICAVERAGECSTPERUNITSNDCUR` | DECIMAL(18,5) |  |  |  |  |
| 31 | `DYNAVGCOSTPERUNBEFADDCSTSNDCUR` | DECIMAL(18,5) |  |  |  |  |
| 32 | `DYNAVGCSTTOTVALBEFADDCSTSNDCUR` | DECIMAL(18,5) |  |  |  |  |
| 33 | `PERCENTCATEGORYSNDCUR1` | DECIMAL(6,3) |  |  |  |  |
| 34 | `PERCENTCATEGORYSNDCUR2` | DECIMAL(6,3) |  |  |  |  |
| 35 | `PERCENTCATEGORYSNDCUR3` | DECIMAL(6,3) |  |  |  |  |
| 36 | `PERCENTCATEGORYSNDCUR4` | DECIMAL(6,3) |  |  |  |  |
| 37 | `PERCENTCATEGORYSNDCUR5` | DECIMAL(6,3) |  |  |  |  |
| 38 | `PERCENTCATEGORYSNDCUR6` | DECIMAL(6,3) |  |  |  |  |
| 39 | `PERCENTCATEGORYSNDCUR7` | DECIMAL(6,3) |  |  |  |  |
| 40 | `PERCENTCATEGORYSNDCUR8` | DECIMAL(6,3) |  |  |  |  |
| 41 | `PERCENTCATEGORYSNDCUR9` | DECIMAL(6,3) |  |  |  |  |
| 42 | `PERCENTCATEGORYSNDCUR10` | DECIMAL(6,3) |  |  |  |  |
| 43 | `PERCENTCATEGORYSNDCUR11` | DECIMAL(6,3) |  |  |  |  |
| 44 | `PERCENTCATEGORYSNDCUR12` | DECIMAL(6,3) |  |  |  |  |
| 45 | `PERCENTCATEGORYSNDCUR0` | DECIMAL(6,3) |  |  |  |  |
| 46 | `PERCENTCATEGORYFIRSTISS1` | DECIMAL(6,3) |  |  |  |  |
| 47 | `PERCENTCATEGORYFIRSTISS2` | DECIMAL(6,3) |  |  |  |  |
| 48 | `PERCENTCATEGORYFIRSTISS3` | DECIMAL(6,3) |  |  |  |  |
| 49 | `PERCENTCATEGORYFIRSTISS4` | DECIMAL(6,3) |  |  |  |  |
| 50 | `PERCENTCATEGORYFIRSTISS5` | DECIMAL(6,3) |  |  |  |  |
| 51 | `PERCENTCATEGORYFIRSTISS6` | DECIMAL(6,3) |  |  |  |  |
| 52 | `PERCENTCATEGORYFIRSTISS7` | DECIMAL(6,3) |  |  |  |  |
| 53 | `PERCENTCATEGORYFIRSTISS8` | DECIMAL(6,3) |  |  |  |  |
| 54 | `PERCENTCATEGORYFIRSTISS9` | DECIMAL(6,3) |  |  |  |  |
| 55 | `PERCENTCATEGORYFIRSTISS10` | DECIMAL(6,3) |  |  |  |  |
| 56 | `PERCENTCATEGORYFIRSTISS11` | DECIMAL(6,3) |  |  |  |  |
| 57 | `PERCENTCATEGORYFIRSTISS12` | DECIMAL(6,3) |  |  |  |  |
| 58 | `PERCENTCATEGORYFIRSTISS0` | DECIMAL(6,3) |  |  |  |  |
| 59 | `PERCENTCATEGORYSNDCURFIRSTISS1` | DECIMAL(6,3) |  |  |  |  |
| 60 | `PERCENTCATEGORYSNDCURFIRSTISS2` | DECIMAL(6,3) |  |  |  |  |
| 61 | `PERCENTCATEGORYSNDCURFIRSTISS3` | DECIMAL(6,3) |  |  |  |  |
| 62 | `PERCENTCATEGORYSNDCURFIRSTISS4` | DECIMAL(6,3) |  |  |  |  |
| 63 | `PERCENTCATEGORYSNDCURFIRSTISS5` | DECIMAL(6,3) |  |  |  |  |
| 64 | `PERCENTCATEGORYSNDCURFIRSTISS6` | DECIMAL(6,3) |  |  |  |  |
| 65 | `PERCENTCATEGORYSNDCURFIRSTISS7` | DECIMAL(6,3) |  |  |  |  |
| 66 | `PERCENTCATEGORYSNDCURFIRSTISS8` | DECIMAL(6,3) |  |  |  |  |
| 67 | `PERCENTCATEGORYSNDCURFIRSTISS9` | DECIMAL(6,3) |  |  |  |  |
| 68 | `PERCENTCTGSNDCURFIRSTISS10` | DECIMAL(6,3) |  |  |  |  |
| 69 | `PERCENTCTGSNDCURFIRSTISS11` | DECIMAL(6,3) |  |  |  |  |
| 70 | `PERCENTCTGSNDCURFIRSTISS12` | DECIMAL(6,3) |  |  |  |  |
| 71 | `PERCENTCATEGORYSNDCURFIRSTISS0` | DECIMAL(6,3) |  |  |  |  |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ACTUALCOSTENTITY_ACTUALCOSTENTITYCLOSINGBALANCE` | `ACTUALCOSTENTITYCOMPANYCODE`, `ACTUALCOSTENTITYNUMBERID` | [`ACTUALCOSTENTITY`](../OTHER/ACTUALCOSTENTITY.md) | `COMPANYCODE`, `NUMBERID` | RESTRICT | `ACTUALCOSTENTITYCLOSINGBLN.ACTUALCOSTENTITYCOMPANYCODE = ACTUALCOSTENTITY.COMPANYCODE AND ACTUALCOSTENTITYCLOSINGBLN.ACTUALCOSTENTITYNUMBERID = ACTUALCOSTENTITY.NUMBERID` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ACTUALCOSTENTITYCLOSINGBLNUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ACTUALCOSTENTITYCOMPANYCODE,
       t.ACTUALCOSTENTITYNUMBERID,
       t.CLOSINGBALANCEFORDATE,
       t.DYNAMICAVERAGECOSTTOTALVALUE,
       t.DYNAMICAVERAGECOSTTOTALQTY,
       t.DYNAMICAVERAGECOSTPERUNIT,
       t.PERCENTCATEGORY1,
       t.PERCENTCATEGORY2,
       t.PERCENTCATEGORY3,
       t.PERCENTCATEGORY4,
       t.PERCENTCATEGORY5,
       t.PERCENTCATEGORY6
FROM   DB2ADMIN.ACTUALCOSTENTITYCLOSINGBLN t
FETCH FIRST 100 ROWS ONLY;
```
