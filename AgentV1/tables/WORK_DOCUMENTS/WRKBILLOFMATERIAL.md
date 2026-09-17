# DB2ADMIN.WRKBILLOFMATERIAL

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 53
- **Primary key**: `COMPANYCODE`, `CREATIONTIMESTAMP`, `PRODUCTITCODE`, `SUBCODE01`, `SUBCODE02`, `SUBCODE03`, `SUBCODE04`, `SUBCODE05`, `SUBCODE06`, `SUBCODE07`, `SUBCODE08`, `SUBCODE09`, `SUBCODE10`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 127945

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 2 | `PRODUCTITCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 3 | `PRODUCTITCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 4 | `SUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 5 | `SUBCODE03` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 6 | `SUBCODE02` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 7 | `SUBCODE04` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 8 | `SUBCODE05` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 9 | `SUBCODE06` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 10 | `SUBCODE07` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 11 | `SUBCODE08` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 12 | `SUBCODE09` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 13 | `SUBCODE10` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 14 | `SUFFIXCODE` | CHAR(20) |  |  |  |  |
| 15 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 16 | `PRODUCTIONBOMMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 17 | `PRODUCTIONREFERENCEBOM` | SMALLINT | NOT NULL |  |  |  |
| 18 | `COSTCALBOMMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 19 | `TECHNICALBOMMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 20 | `PLANNINGBOMMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 21 | `BOMUOMTYPE` | CHAR(12) |  |  |  |  |
| 22 | `BOMUOMCODECODE` | CHAR(3) |  |  |  |  |
| 23 | `STATUS` | CHAR(1) | NOT NULL |  |  |  |
| 24 | `INCIDENCE` | INTEGER | NOT NULL |  |  |  |
| 25 | `PLANTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 26 | `PLANTCODE` | CHAR(8) |  |  |  |  |
| 27 | `COSTGROUPCODE` | CHAR(3) |  |  |  |  |
| 28 | `STAGE` | INTEGER | NOT NULL |  |  |  |
| 29 | `BUYERREFERENCE01` | CHAR(50) |  |  |  |  |
| 30 | `BUYERREFERENCE02` | CHAR(50) |  |  |  |  |
| 31 | `BUYERREFERENCE03` | CHAR(50) |  |  |  |  |
| 32 | `BUYERREFERENCE04` | CHAR(50) |  |  |  |  |
| 33 | `BUYERREFERENCE05` | CHAR(50) |  |  |  |  |
| 34 | `BUYERREFERENCE06` | CHAR(50) |  |  |  |  |
| 35 | `BUYERREFERENCE07` | CHAR(50) |  |  |  |  |
| 36 | `BUYERREFERENCE08` | CHAR(50) |  |  |  |  |
| 37 | `BUYERREFERENCE09` | CHAR(50) |  |  |  |  |
| 38 | `BUYERREFERENCE10` | CHAR(50) |  |  |  |  |
| 39 | `PLANTCOMMENTS01` | CHAR(50) |  |  |  |  |
| 40 | `PLANTCOMMENTS02` | CHAR(50) |  |  |  |  |
| 41 | `PLANTCOMMENTS03` | CHAR(50) |  |  |  |  |
| 42 | `PLANTCOMMENTS04` | CHAR(50) |  |  |  |  |
| 43 | `PLANTCOMMENTS05` | CHAR(50) |  |  |  |  |
| 44 | `PLANTCOMMENTS06` | CHAR(50) |  |  |  |  |
| 45 | `PLANTCOMMENTS07` | CHAR(50) |  |  |  |  |
| 46 | `PLANTCOMMENTS08` | CHAR(50) |  |  |  |  |
| 47 | `PLANTCOMMENTS09` | CHAR(50) |  |  |  |  |
| 48 | `PLANTCOMMENTS10` | CHAR(50) |  |  |  |  |
| 49 | `COSTING` | DECIMAL(18,5) |  |  |  |  |
| 50 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 51 | `COSTCENTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 52 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKBILLOFMATERIALUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CREATIONTIMESTAMP,
       t.PRODUCTITCOMPANYCODE,
       t.PRODUCTITCODE,
       t.SUBCODE01,
       t.SUBCODE03,
       t.SUBCODE02,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06,
       t.SUBCODE07,
       t.SUBCODE08
FROM   DB2ADMIN.WRKBILLOFMATERIAL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
