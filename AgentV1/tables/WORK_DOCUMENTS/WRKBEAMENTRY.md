# DB2ADMIN.WRKBEAMENTRY

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 36
- **Primary key**: `COMPANYCODE`, `MACHINECODE`, `POSTINGDATE`, `PLANTCODE`, `WORKCENTERCODE`, `SHIFT`, `TEMPLATECODE`, `CREATIONUSER`, `CREATIONTIMESTAMP`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 130653

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `MACHINECODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 2 | `SHIFT` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 3 | `SHIFTMANAGERCODE` | CHAR(8) |  |  |  |  |
| 4 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 5 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 6 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 7 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 8 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 9 | `POSTINGDATE` | DATE | NOT NULL | PK | primary_key |  |
| 10 | `PLANTCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 11 | `PLANTCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 12 | `WORKCENTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 13 | `PRODUCTIONORDERCODE` | CHAR(15) |  |  |  |  |
| 14 | `PRODUCTIONDEMANDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 15 | `PRODUCTIONDEMANDCODE` | CHAR(15) |  |  |  |  |
| 16 | `NEWDEMANDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 17 | `NEWDEMANDCODE` | CHAR(15) |  |  |  |  |
| 18 | `TEMPLATECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 19 | `NEWBEAMST` | TIME |  |  |  |  |
| 20 | `MECHANIC1CODE` | CHAR(8) |  |  |  |  |
| 21 | `MECHANIC2CODE` | CHAR(8) |  |  |  |  |
| 22 | `QUALITYCHECKERCODE` | CHAR(8) |  |  |  |  |
| 23 | `ITEMTYPE1COMPANYCODE` | CHAR(3) |  |  |  |  |
| 24 | `ITEMTYPE1CODE` | CHAR(3) |  |  |  |  |
| 25 | `ITEMDESC` | VARCHAR(120) |  |  |  |  |
| 26 | `LOOMRPM` | INTEGER | NOT NULL |  |  |  |
| 27 | `BEAMCHANGETYPE` | CHAR(1) |  |  |  |  |
| 28 | `PHYSICALBEAMNO` | CHAR(6) |  |  |  |  |
| 29 | `BEAMLENGTH` | INTEGER | NOT NULL |  |  |  |
| 30 | `CREATIONUSER` | CHAR(50) | NOT NULL | PK | primary_key audit | User who created the row (audit). |
| 31 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 32 | `REMOVE1` | INTEGER | NOT NULL |  |  |  |
| 33 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 34 | `TEMPLATECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 35 | `OPERATIONCODE` | CHAR(8) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKBEAMENTRYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.MACHINECODE,
       t.SHIFT,
       t.SHIFTMANAGERCODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.POSTINGDATE,
       t.PLANTCOMPANYCODE,
       t.PLANTCODE
FROM   DB2ADMIN.WRKBEAMENTRY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
