# DB2ADMIN.PATTERNLEVEL

- **Module**: `PRODUCTION` (low confidence — table name starts with 'PATTERN')
- **Roles**: `business_data`
- **Columns**: 30
- **Primary key**: `PATTERNHEADERCOMPANYCODE`, `PATTERNHEADERWARPWEFTTYPE`, `PATTERNHEADERPATTERNCODE`, `WARPWEFTLEVEL`
- **FK degree**: referenced by 2 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 17057

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PATTERNHEADERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `PATTERNHEADERWARPWEFTTYPE` | CHAR(1) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `PATTERNHEADERPATTERNCODE` | CHAR(20) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `WARPWEFTLEVEL` | DECIMAL(2,0) | NOT NULL | PK | primary_key |  |
| 4 | `LVLNOOFENDS` | DECIMAL(7,0) |  |  |  |  |
| 5 | `LVLNOOFENDSEXTRA` | DECIMAL(11,4) |  |  |  |  |
| 6 | `LVLREEDWIDTH` | DECIMAL(11,4) |  |  |  |  |
| 7 | `LVLREEDWIDTHEXTRA` | DECIMAL(11,4) |  |  |  |  |
| 8 | `LVLWASTEPERCENT` | DECIMAL(5,2) |  |  |  |  |
| 9 | `LVLNOOFYARNSFORUOM` | DECIMAL(11,4) |  |  |  |  |
| 10 | `LVLMULTIPLIER` | DECIMAL(5,0) |  |  |  |  |
| 11 | `ITEMTYPEAFICODE` | CHAR(3) |  | FK | foreign_key |  |
| 12 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 13 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 19 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 20 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 21 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 22 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 23 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 24 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 25 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 26 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 27 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 28 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 29 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ITEMTYPE_ITEMTYPEAFI` | `ITEMTYPEAFICOMPANYCODE`, `ITEMTYPEAFICODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PATTERNLEVEL.ITEMTYPEAFICOMPANYCODE = ITEMTYPE.COMPANYCODE AND PATTERNLEVEL.ITEMTYPEAFICODE = ITEMTYPE.CODE` |
| `PATTERNHEADER_PATTERNLEVEL` | `PATTERNHEADERCOMPANYCODE`, `PATTERNHEADERWARPWEFTTYPE`, `PATTERNHEADERPATTERNCODE` | [`PATTERNHEADER`](../PRODUCTION/PATTERNHEADER.md) | `COMPANYCODE`, `WARPWEFTTYPE`, `PATTERNCODE` | RESTRICT | `PATTERNLEVEL.PATTERNHEADERCOMPANYCODE = PATTERNHEADER.COMPANYCODE AND PATTERNLEVEL.PATTERNHEADERWARPWEFTTYPE = PATTERNHEADER.WARPWEFTTYPE AND PATTERNLEVEL.PATTERNHEADERPATTERNCODE = PATTERNHEADER.PATTERNCODE` |

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `PATTERNLEVEL_PATTERNDETAIL` | [`PATTERNDETAIL`](../PRODUCTION/PATTERNDETAIL.md) | `PATLVLPATHEADERCOMPANYCODE`, `PATLVLPATHEADERWARPWEFTTYPE`, `PATLVLPATHEADERPATTERNCODE`, `PATTERNLEVELWARPWEFTLEVEL` | `PATTERNDETAIL.PATLVLPATHEADERCOMPANYCODE = PATTERNLEVEL.PATTERNHEADERCOMPANYCODE AND PATTERNDETAIL.PATLVLPATHEADERWARPWEFTTYPE = PATTERNLEVEL.PATTERNHEADERWARPWEFTTYPE AND PATTERNDETAIL.PATLVLPATHEADERPATTERNCODE = PATTERNLEVEL.PATTERNHEADERPATTERNCODE AND PATTERNDETAIL.PATTERNLEVELWARPWEFTLEVEL = PATTERNLEVEL.WARPWEFTLEVEL` |
| `PATTERNLEVEL_PATTERNREPETITION` | [`PATTERNREPETITION`](../PRODUCTION/PATTERNREPETITION.md) | `PATLVLPATHEADERCOMPANYCODE`, `PATLVLPATHEADERWARPWEFTTYPE`, `PATLVLPATHEADERPATTERNCODE`, `PATTERNLEVELWARPWEFTLEVEL` | `PATTERNREPETITION.PATLVLPATHEADERCOMPANYCODE = PATTERNLEVEL.PATTERNHEADERCOMPANYCODE AND PATTERNREPETITION.PATLVLPATHEADERWARPWEFTTYPE = PATTERNLEVEL.PATTERNHEADERWARPWEFTTYPE AND PATTERNREPETITION.PATLVLPATHEADERPATTERNCODE = PATTERNLEVEL.PATTERNHEADERPATTERNCODE AND PATTERNREPETITION.PATTERNLEVELWARPWEFTLEVEL = PATTERNLEVEL.WARPWEFTLEVEL` |

## Indexes

- `PATTERNLEVELUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.PATTERNHEADERCOMPANYCODE,
       t.PATTERNHEADERWARPWEFTTYPE,
       t.PATTERNHEADERPATTERNCODE,
       t.WARPWEFTLEVEL,
       t.LVLNOOFENDS,
       t.LVLNOOFENDSEXTRA,
       t.LVLREEDWIDTH,
       t.LVLREEDWIDTHEXTRA,
       t.LVLWASTEPERCENT,
       t.LVLNOOFYARNSFORUOM,
       t.LVLMULTIPLIER,
       t.ITEMTYPEAFICODE
FROM   DB2ADMIN.PATTERNLEVEL t
FETCH FIRST 100 ROWS ONLY;
```
