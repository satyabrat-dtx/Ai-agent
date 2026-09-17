# DB2ADMIN.WRKDOFFENTRY

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 26
- **Primary key**: `COMPANYCODE`, `MACHINECODE`, `ITEMTYPECODE`, `POSTINGDATE`, `PLANTCODE`, `WORKCENTERCODE`, `SHIFT`, `TEMPLATECODE`, `CREATIONUSER`, `CREATIONTIMESTAMP`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 130860

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `MACHINECODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 6 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 7 | `POSTINGDATE` | DATE | NOT NULL | PK | primary_key |  |
| 8 | `PLANTCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 9 | `PLANTCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 10 | `WORKCENTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 11 | `SHIFT` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 12 | `DTIME` | TIME |  |  |  |  |
| 13 | `PRODUCTIONORDERCODE` | CHAR(15) |  |  |  |  |
| 14 | `TEMPLATECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 15 | `CREATIONUSER` | CHAR(50) | NOT NULL | PK | primary_key audit | User who created the row (audit). |
| 16 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 17 | `GROSSWEIGHT` | DECIMAL(18,5) |  |  |  |  |
| 18 | `TAREWEIGHT` | DECIMAL(18,5) |  |  |  |  |
| 19 | `NETWEIGHT` | DECIMAL(18,5) |  |  |  |  |
| 20 | `ELEMENTCODE` | CHAR(10) |  |  |  |  |
| 21 | `PRODUCTIONDEMANDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 22 | `PRODUCTIONDEMANDCODE` | CHAR(15) |  |  |  |  |
| 23 | `REMOVE1` | INTEGER | NOT NULL |  |  |  |
| 24 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 25 | `TEMPLATECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKDOFFENTRYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.MACHINECODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.POSTINGDATE,
       t.PLANTCOMPANYCODE,
       t.PLANTCODE,
       t.WORKCENTERCODE,
       t.SHIFT
FROM   DB2ADMIN.WRKDOFFENTRY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
