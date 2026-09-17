# DB2ADMIN.RULECHOOSEKEYS

- **Module**: `LOCALIZATION` (low confidence — FK neighbourhood: 1 of 1 related tables are LOCALIZATION)
- **Roles**: `business_data`
- **Columns**: 87
- **Primary key**: `RULECOMPANYCODE`, `RULECODE`, `SEQUENCE`
- **FK degree**: referenced by 1 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 24625

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `RULECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `RULECODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SEQUENCE` | DECIMAL(2,0) | NOT NULL | PK | primary_key |  |
| 3 | `RULETEMPLATECODE` | CHAR(3) |  | FK | foreign_key |  |
| 4 | `USECOLUMN1` | SMALLINT | NOT NULL |  |  |  |
| 5 | `IDENTIFIER1` | DECIMAL(3,0) |  |  |  |  |
| 6 | `USECOLUMN2` | SMALLINT | NOT NULL |  |  |  |
| 7 | `IDENTIFIER2` | DECIMAL(3,0) |  |  |  |  |
| 8 | `USECOLUMN3` | SMALLINT | NOT NULL |  |  |  |
| 9 | `IDENTIFIER3` | DECIMAL(3,0) |  |  |  |  |
| 10 | `USECOLUMN4` | SMALLINT | NOT NULL |  |  |  |
| 11 | `IDENTIFIER4` | DECIMAL(3,0) |  |  |  |  |
| 12 | `USECOLUMN5` | SMALLINT | NOT NULL |  |  |  |
| 13 | `IDENTIFIER5` | DECIMAL(3,0) |  |  |  |  |
| 14 | `USECOLUMN6` | SMALLINT | NOT NULL |  |  |  |
| 15 | `IDENTIFIER6` | DECIMAL(3,0) |  |  |  |  |
| 16 | `USECOLUMN7` | SMALLINT | NOT NULL |  |  |  |
| 17 | `IDENTIFIER7` | DECIMAL(3,0) |  |  |  |  |
| 18 | `USECOLUMN8` | SMALLINT | NOT NULL |  |  |  |
| 19 | `IDENTIFIER8` | DECIMAL(3,0) |  |  |  |  |
| 20 | `USECOLUMN9` | SMALLINT | NOT NULL |  |  |  |
| 21 | `IDENTIFIER9` | DECIMAL(3,0) |  |  |  |  |
| 22 | `USECOLUMN10` | SMALLINT | NOT NULL |  |  |  |
| 23 | `IDENTIFIER10` | DECIMAL(3,0) |  |  |  |  |
| 24 | `USECOLUMN11` | SMALLINT | NOT NULL |  |  |  |
| 25 | `IDENTIFIER11` | DECIMAL(3,0) |  |  |  |  |
| 26 | `USECOLUMN12` | SMALLINT | NOT NULL |  |  |  |
| 27 | `IDENTIFIER12` | DECIMAL(3,0) |  |  |  |  |
| 28 | `USECOLUMN13` | SMALLINT | NOT NULL |  |  |  |
| 29 | `IDENTIFIER13` | DECIMAL(3,0) |  |  |  |  |
| 30 | `USECOLUMN14` | SMALLINT | NOT NULL |  |  |  |
| 31 | `IDENTIFIER14` | DECIMAL(3,0) |  |  |  |  |
| 32 | `USECOLUMN15` | SMALLINT | NOT NULL |  |  |  |
| 33 | `IDENTIFIER15` | DECIMAL(3,0) |  |  |  |  |
| 34 | `USECOLUMN16` | SMALLINT | NOT NULL |  |  |  |
| 35 | `IDENTIFIER16` | DECIMAL(3,0) |  |  |  |  |
| 36 | `USECOLUMN17` | SMALLINT | NOT NULL |  |  |  |
| 37 | `IDENTIFIER17` | DECIMAL(3,0) |  |  |  |  |
| 38 | `USECOLUMN18` | SMALLINT | NOT NULL |  |  |  |
| 39 | `IDENTIFIER18` | DECIMAL(3,0) |  |  |  |  |
| 40 | `USECOLUMN19` | SMALLINT | NOT NULL |  |  |  |
| 41 | `IDENTIFIER19` | DECIMAL(3,0) |  |  |  |  |
| 42 | `USECOLUMN20` | SMALLINT | NOT NULL |  |  |  |
| 43 | `IDENTIFIER20` | DECIMAL(3,0) |  |  |  |  |
| 44 | `USECOLUMN21` | SMALLINT | NOT NULL |  |  |  |
| 45 | `IDENTIFIER21` | DECIMAL(3,0) |  |  |  |  |
| 46 | `USECOLUMN22` | SMALLINT | NOT NULL |  |  |  |
| 47 | `IDENTIFIER22` | DECIMAL(3,0) |  |  |  |  |
| 48 | `USECOLUMN23` | SMALLINT | NOT NULL |  |  |  |
| 49 | `IDENTIFIER23` | DECIMAL(3,0) |  |  |  |  |
| 50 | `USECOLUMN24` | SMALLINT | NOT NULL |  |  |  |
| 51 | `IDENTIFIER24` | DECIMAL(3,0) |  |  |  |  |
| 52 | `USECOLUMN25` | SMALLINT | NOT NULL |  |  |  |
| 53 | `IDENTIFIER25` | DECIMAL(3,0) |  |  |  |  |
| 54 | `OUTIDENTIFIER1` | DECIMAL(3,0) |  |  |  |  |
| 55 | `OUTIDENTIFIER2` | DECIMAL(3,0) |  |  |  |  |
| 56 | `OUTIDENTIFIER3` | DECIMAL(3,0) |  |  |  |  |
| 57 | `OUTIDENTIFIER4` | DECIMAL(3,0) |  |  |  |  |
| 58 | `OUTIDENTIFIER5` | DECIMAL(3,0) |  |  |  |  |
| 59 | `OUTIDENTIFIER6` | DECIMAL(3,0) |  |  |  |  |
| 60 | `OUTIDENTIFIER7` | DECIMAL(3,0) |  |  |  |  |
| 61 | `OUTIDENTIFIER8` | DECIMAL(3,0) |  |  |  |  |
| 62 | `OUTIDENTIFIER9` | DECIMAL(3,0) |  |  |  |  |
| 63 | `OUTIDENTIFIER10` | DECIMAL(3,0) |  |  |  |  |
| 64 | `OUTIDENTIFIER11` | DECIMAL(3,0) |  |  |  |  |
| 65 | `OUTIDENTIFIER12` | DECIMAL(3,0) |  |  |  |  |
| 66 | `OUTIDENTIFIER13` | DECIMAL(3,0) |  |  |  |  |
| 67 | `OUTIDENTIFIER14` | DECIMAL(3,0) |  |  |  |  |
| 68 | `OUTIDENTIFIER15` | DECIMAL(3,0) |  |  |  |  |
| 69 | `OUTIDENTIFIER16` | DECIMAL(3,0) |  |  |  |  |
| 70 | `OUTIDENTIFIER17` | DECIMAL(3,0) |  |  |  |  |
| 71 | `OUTIDENTIFIER18` | DECIMAL(3,0) |  |  |  |  |
| 72 | `OUTIDENTIFIER19` | DECIMAL(3,0) |  |  |  |  |
| 73 | `OUTIDENTIFIER20` | DECIMAL(3,0) |  |  |  |  |
| 74 | `OUTIDENTIFIER21` | DECIMAL(3,0) |  |  |  |  |
| 75 | `OUTIDENTIFIER22` | DECIMAL(3,0) |  |  |  |  |
| 76 | `OUTIDENTIFIER23` | DECIMAL(3,0) |  |  |  |  |
| 77 | `OUTIDENTIFIER24` | DECIMAL(3,0) |  |  |  |  |
| 78 | `OUTIDENTIFIER25` | DECIMAL(3,0) |  |  |  |  |
| 79 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 80 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 81 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 82 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 83 | `DESCRIPTION` | CHAR(100) |  |  | description |  |
| 84 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 85 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 86 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `RULES_RULECHOOSEKEYS` | `RULECOMPANYCODE`, `RULECODE` | [`RULES`](../CORE_MASTER/RULES.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RULECHOOSEKEYS.RULECOMPANYCODE = RULES.COMPANYCODE AND RULECHOOSEKEYS.RULECODE = RULES.CODE` |
| `RULETEMPLATEHEADER_RULETEMPLATE` | `RULECOMPANYCODE`, `RULETEMPLATECODE` | [`RULETEMPLATEHEADER`](../LOCALIZATION/RULETEMPLATEHEADER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RULECHOOSEKEYS.RULECOMPANYCODE = RULETEMPLATEHEADER.COMPANYCODE AND RULECHOOSEKEYS.RULETEMPLATECODE = RULETEMPLATEHEADER.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `RULECHOOSEKEYS_RULECHOOSEKEYS` | [`RULEDEFINITIONHEADER`](../LOCALIZATION/RULEDEFINITIONHEADER.md) | `COMPANYCODE`, `RULECODE`, `RULECHOOSEKEYSSEQUENCE` | `RULEDEFINITIONHEADER.COMPANYCODE = RULECHOOSEKEYS.RULECOMPANYCODE AND RULEDEFINITIONHEADER.RULECODE = RULECHOOSEKEYS.RULECODE AND RULEDEFINITIONHEADER.RULECHOOSEKEYSSEQUENCE = RULECHOOSEKEYS.SEQUENCE` |

## Indexes

- `RULECHOOSEKEYSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.RULECOMPANYCODE,
       t.RULECODE,
       t.SEQUENCE,
       t.RULETEMPLATECODE,
       t.USECOLUMN1,
       t.IDENTIFIER1,
       t.USECOLUMN2,
       t.IDENTIFIER2,
       t.USECOLUMN3,
       t.IDENTIFIER3,
       t.USECOLUMN4,
       t.IDENTIFIER4
FROM   DB2ADMIN.RULECHOOSEKEYS t
FETCH FIRST 100 ROWS ONLY;
```
